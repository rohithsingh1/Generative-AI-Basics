import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,LabelEncoder

## Load the dataset
data = pd.read_csv('./training_data/Churn_Modelling.csv')
print(data.head())





## Preprocess the data
### Drop irrelevant columns
'''
axis=0 vs axis=1 in drop()

- axis=0 (the default) means rows. Pandas looks for the labels in the index (row labels).
- axis=1 means columns. Pandas looks for the labels in the column names.

What happens with axis=0 in your code

data = data.drop(['RowNumber','CustomerId','Surname'], axis=0)

Pandas will look for rows whose index label is 'RowNumber', 'CustomerId' or 
'Surname'. Your index is probably the default 0, 1, 2, …, so no row has those labels, and you get:

KeyError: "['RowNumber', 'CustomerId', 'Surname'] not found in axis"
'''
print('===============================Preprocess data part 1 ============================\n')
data = data.drop(['RowNumber','CustomerId','Surname'],axis=1)
print(data.head())
print('===============================Preprocess data part 1 ============================\n')






## Encode categorical variables
print('===============================Encode categorical variables 1 ============================\n')
'''
These lines make a translator, show it the Gender column so it learns Female → 0 and Male → 1, and 
then replace the words in that column with those numbers.

The computer only understands numbers. So this code changes "Female" to 0 and "Male" to 1 in the Gender column.
'''
label_encoder_gender = LabelEncoder()
# print(data['Gender'])
# print(type(data['Gender']))
data["Gender"] = np.asarray(label_encoder_gender.fit_transform(data['Gender']))
print(data.head())
print('===============================Encode categorical variables 1 ============================\n')






## Onehot encode 'Geography'
## Scope of improvement can we use word_2_vec vector encoding ?
from sklearn.preprocessing import OneHotEncoder

print('===============================Onehot encode Geography ============================\n')

onehot_encoder_geo = OneHotEncoder(sparse_output=False)
# print(data[['Geography']])
# print(type(data[['Geography']]))
# print(data[['Geography',"Age","Gender"]]) # [10000 rows x 3 columns]
# print(data[['Geography',"Age","Gender"]].shape) # (10000, 3)
geo_encoder = onehot_encoder_geo.fit_transform(data[['Geography']])
print(geo_encoder)

geo_feature_names = onehot_encoder_geo.get_feature_names_out(['Geography'])
print(geo_feature_names)

geo_encoder_df = pd.DataFrame(geo_encoder,columns=geo_feature_names)
print(geo_encoder_df)
print('===============================Onehot encode Geography ============================\n')






## Combine one hot encoder columns with the original data
print('===============================Combine one hot encoder columns with the original data ============================\n')

data = pd.concat([data.drop(['Geography'],axis=1),geo_encoder_df],axis=1)
print(data)

print('===============================Combine one hot encoder columns with the original data ============================\n')










## Save the encoders and scaler
print('===============================Save the encoders and scaler ============================\n')
import pickle


with open('./pkl/label_encoder_gender.pkl','wb') as file:
    pickle.dump(label_encoder_gender,file=file)

with open('./pkl/onehot_encoder_geo.pkl','wb') as file:
    pickle.dump(onehot_encoder_geo,file=file)

print('===============================Save the encoders and scaler ============================\n')










## DiVide the dataset into indepent and dependent features
print('===============================DiVide the dataset into indepent and dependent features ============================\n')

X = data.drop(['Exited'],axis=1)
Y = data['Exited']


## Split the data in training and tetsing sets
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

## Scale these features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(X_train)


with open('./pkl/scaler.pkl','wb') as file:
    pickle.dump(scaler,file=file)

print('===============================DiVide the dataset into indepent and dependent features ============================\n')










##### ### ANN Implementation
import tensorflow as tf
from keras import Sequential , Input
from keras.layers import Dense
from keras.optimizers import Adam
from keras.losses import BinaryCrossentropy
import datetime


## Build Our ANN Model
print('===============================Build Our ANN Model ============================\n')
'''
ReLU: used in the middle (hidden) layers

Rule: if the number is negative, make it 0. Otherwise keep it as it is.

−5 → 0
−1 → 0
 3 → 3
 8 → 8

Sigmoid: used in the last (output) layer

Rule: squeeze any number into the range 0 to 1.

−5 → 0.01
 0 → 0.5
 2 → 0.88
 5 → 0.99

'''
model = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(64,activation="relu"),
    Dense(32, activation='relu'),       # HL2
    Dense(1, activation='sigmoid')
])

print(model.summary())

print('===============================Build Our ANN Model ============================\n')









## compile the model

print('===============================compile the model ============================\n')
opt = Adam(learning_rate=0.01)
loss = BinaryCrossentropy()
model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])

print('===============================compile the model ============================\n')








## Set up the Tensorboard
from keras.callbacks import EarlyStopping , TensorBoard
log_dir = "logs/fit/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

tensorflow_callback = TensorBoard(log_dir=log_dir,histogram_freq=1)

## Set up Early Stopping
early_stopping_callback = EarlyStopping(monitor="val_loss",patience=10,restore_best_weights=True)





### Train the model
history = model.fit(X_train,Y_train,validation_data=(X_test,Y_test),epochs=100,callbacks=[tensorflow_callback,early_stopping_callback])

print(history)



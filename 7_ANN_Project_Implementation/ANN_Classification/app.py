import pickle
import pandas as pd
from keras.models import load_model
from keras import Model
from typing import cast
import numpy as np
import streamlit as st
from sklearn.preprocessing import LabelEncoder , OneHotEncoder , StandardScaler

### Load the trained model, scaler pickle,onehot

model = cast(Model,load_model("./model/model.keras"))


## load the encoder and scaler

with open('./pkl/onehot_encoder_geo.pkl','rb') as file:
    geo_one_hot_encoder: OneHotEncoder = pickle.load(file)

with open('./pkl/label_encoder_gender.pkl','rb') as file:
    gender_label_encoder:LabelEncoder = pickle.load(file=file)

with open('./pkl/scaler.pkl','rb') as file:
    scaler: StandardScaler = pickle.load(file)


## streamlit app

st.title('ANN Classification Prediction')

# User input

geography_default_value = np.asarray(geo_one_hot_encoder.categories_[0]).tolist()
geography = st.selectbox('Geography',geography_default_value)
gender = st.selectbox("Gender",gender_label_encoder.classes_)
age = st.slider('Age',18,max_value=92)
balance = st.number_input("Balance",min_value=5000)
credit_score = st.number_input("Credit Score",min_value=500)
estimated_salary = st.number_input('Estimated Salary',min_value=100000)
tensure = st.slider("Tenure",min_value=0,max_value=10)
num_of_products = st.slider('Number of Products',min_value=1,max_value=4)
has_cr_card = st.selectbox("Has Credit Card",[0,1])
is_active_member = st.selectbox("Is Active Member",[0,1])

# Prepare the input data

input_data = [ {
    'CreditScore': credit_score,
    'Geography': geography,
    'Gender': gender,
    'Age': age,
    'Tenure': tensure,
    'Balance': balance,
    'NumOfProducts': num_of_products,
    'HasCrCard': has_cr_card,
    'IsActiveMember': is_active_member,
    'EstimatedSalary': estimated_salary
}]

input_data_df = pd.DataFrame(input_data)

# gender label encoder transform
input_data_df['Gender'] = np.asarray(gender_label_encoder.transform(input_data_df['Gender']))

# geography one hot encoder transform
geo_encoder = np.asarray(geo_one_hot_encoder.transform(input_data_df[['Geography']]))

geo_encoder_title = geo_one_hot_encoder.get_feature_names_out(['Geography'])

geo_encoder_df = pd.DataFrame(geo_encoder,columns=geo_encoder_title)



# combine input Dataframe and Geo one hot encoder DataFrame

new_input_data_df = pd.concat([input_data_df.drop("Geography",axis=1),geo_encoder_df],axis=1)


# scale the all input columns
scaled_input = scaler.transform(new_input_data_df)


# predicting the input from trained model
predicted_value = cast(np.ndarray,model.predict(scaled_input))

prediction_probability = predicted_value[0][0]

st.write(f'Churn Probability: {prediction_probability}')

if prediction_probability > 0.5:
    st.write('The customer is likely to churn.')
else:
    st.write('The customer is not likely to churn.')
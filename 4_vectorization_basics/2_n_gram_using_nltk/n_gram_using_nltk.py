import pandas as pd

messages = pd.read_csv("../../data/TF_IDF_sampleData.csv",names=["label",'message'])

print(messages)

from pathlib import Path

import nltk

nltk_data_dir = Path(__file__).resolve().parents[2] / "nltk_data"
nltk.data.path.append(str(nltk_data_dir))

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords", download_dir=str(nltk_data_dir))


from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

wordNetLemmatizerObj = WordNetLemmatizer()
modified_sentenses = []
stopwords_set = set(stopwords.words('english')) - {'not','no','nor'} 
for i in range(len(messages)):
    review = re.sub('[^a-zA-Z]',' ',messages["message"][i])
    review = review.lower()
    list_of_words = review.split(' ')
    list_of_lemmitizar_words = []
    for word in list_of_words:
        if word not in stopwords_set:
            list_of_lemmitizar_words.append(wordNetLemmatizerObj.lemmatize(word,pos='v'))

    modified_review = ' '.join(list_of_lemmitizar_words)
    modified_sentenses.append(modified_review)

print(modified_sentenses)


## Create the Bag OF Words model
from sklearn.feature_extraction.text import CountVectorizer

## for Binary BOW enable binary=True
countVectorizerObj = CountVectorizer(max_features=30,ngram_range=(1,1))

x = countVectorizerObj.fit_transform(modified_sentenses)
print("Vocabulary:", countVectorizerObj.vocabulary_)
# print(type(X))

# Transformed matrix (rows = sentences, columns = words in vocabulary_ index order)
# fit_transform returns a sparse matrix; Pylance's type hints can't see .toarray(), so ignore that warning here
x_array = x.toarray()  # pyright: ignore[reportAttributeAccessIssue]
print("Feature matrix:\n", x_array)

# Total count of each word across all sentences
frequency_of_words = x_array.sum(axis=0)
print(f"frequency_of_words : {frequency_of_words} , type :",type(frequency_of_words))

ziping_of_words = list(zip(countVectorizerObj.get_feature_names_out(),frequency_of_words))
print(f"ziping_of_words : {ziping_of_words}")
word_counts = dict(ziping_of_words)
print("Word counts:", word_counts)

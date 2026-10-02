
from pathlib import Path

import nltk

nltk_data_dir = Path(__file__).resolve().parents[2] / "nltk_data"
nltk.data.path.append(str(nltk_data_dir))

try:
    nltk.data.find("corpus/stopwords")
except LookupError:
    nltk.download("stopwords", download_dir=str(nltk_data_dir))

from nltk.corpus import stopwords


paragraph = """I have three visions for India. In 3000 years of our history, people from all over 
               the world have come and invaded us, captured our lands, conquered our minds. 
               From Alexander onwards, the Greeks, the Turks, the Moguls, the Portuguese, the British,
               the French, the Dutch, all of them came and looted us, took over what was ours. 
               Yet we have not done this to any other nation. We have not conquered anyone. 
               We have not grabbed their land, their culture, 
               their history and tried to enforce our way of life on them. 
               Why? Because we respect the freedom of others.That is why my 
               first vision is that of freedom. I believe that India got its first vision of 
               this in 1857, when we started the War of Independence. It is this freedom that
               we must protect and nurture and build on. If we are not free, no one will respect us.
               My second vision for India’s development. For fifty years we have been a developing nation.
               It is time we see ourselves as a developed nation. We are among the top 5 nations of the world
               in terms of GDP. We have a 10 percent growth rate in most areas. Our poverty levels are falling.
               Our achievements are being globally recognised today. Yet we lack the self-confidence to
               see ourselves as a developed nation, self-reliant and self-assured. Isn’t this incorrect?
               I have a third vision. India must stand up to the world. Because I believe that unless India 
               stands up to the world, no one will respect us. Only strength respects strength. We must be 
               strong not only as a military power but also as an economic power. Both must go hand-in-hand. 
               My good fortune was to have worked with three great minds. Dr. Vikram Sarabhai of the Dept. of 
               space, Professor Satish Dhawan, who succeeded him and Dr. Brahm Prakash, father of nuclear material.
               I was lucky to have worked with all three of them closely and consider this the great opportunity of my life. 
               I see four milestones in my career"""


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


list_of_sentenses = sent_tokenize(paragraph)
wordNetLemmatizerObj = WordNetLemmatizer()

# new_sentenses_list = []
# for sentense in list_of_sentenses:
#     words_list = word_tokenize(sentense)
#     stemming_words = ''
#     for word in words_list:
#         lowerCaseWord = word.lower()
#         if lowerCaseWord not in set(stopwords.words('english')):
#             stemming_words = stemming_words + ' ' + wordNetLemmatizerObj.lemmatize(lowerCaseWord,pos='v')
#     new_sentenses_list.append(stemming_words)

# print(new_sentenses_list)


list_of_words = word_tokenize(paragraph)

stemming_words_list = []
for word in list_of_words:
    lowerCaseWord = word.lower()
    if lowerCaseWord not in set(stopwords.words('english')):
        stemming_words_list.append(wordNetLemmatizerObj.lemmatize(lowerCaseWord,pos='v'))


print(' '.join(stemming_words_list))




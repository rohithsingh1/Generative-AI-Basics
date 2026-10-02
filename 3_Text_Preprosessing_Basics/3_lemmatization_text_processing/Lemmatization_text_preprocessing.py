
## Q&A,chatbots,text summarization

from pathlib import Path

import nltk

nltk_data_dir = Path(__file__).resolve().parents[2] / "nltk_data"
nltk.data.path.append(str(nltk_data_dir))

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet", download_dir=str(nltk_data_dir))


from nltk.stem import WordNetLemmatizer

wordNetLemmatizerObj = WordNetLemmatizer()

'''
POS- Noun-n
verb-v
adjective-a
adverb-r
'''

print(wordNetLemmatizerObj.lemmatize("going",pos='v'))

words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]

for word in words:
    print(word+"---->"+wordNetLemmatizerObj.lemmatize(word,pos='v'))


print(wordNetLemmatizerObj.lemmatize("fairly",pos='v'),wordNetLemmatizerObj.lemmatize("sportingly",pos="v"))

print(wordNetLemmatizerObj.lemmatize('congratulations',pos='v'))

print(wordNetLemmatizerObj.lemmatize('congratulations',pos='a'))

print(wordNetLemmatizerObj.lemmatize('congratulations',pos='r'))
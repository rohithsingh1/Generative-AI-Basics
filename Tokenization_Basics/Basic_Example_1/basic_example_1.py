
from pathlib import Path

import nltk

nltk_data_dir = Path(__file__).resolve().parents[2] / "nltk_data"
# Tell NLTK to also search inside our project nltk_data folder.
# NLTK, please check this folder also when looking for downloaded resources.
nltk.data.path.append(str(nltk_data_dir))

try:
    nltk.data.find("tokenizers/punkt_tab")
except LookupError:
    nltk.download("punkt_tab", download_dir=str(nltk_data_dir))

corpus="""Hello Welcome,to Krish Naik's NLP Tutorials.
Please do watch the entire course! to become expert in NLP.
"""


##  Tokenization
## Sentence-->paragraphs
print("==============================sent_tokenize ===============\n")
from nltk.tokenize import sent_tokenize
documents = sent_tokenize(corpus)
print(documents)
print("==============================sent_tokenize ===============\n")


## Tokenization 
## Paragraph-->words
## sentence--->words
print("==============================word_tokenize ===============\n")
from nltk.tokenize import word_tokenize
words_list = word_tokenize(corpus)
print(words_list)
print("==============================word_tokenize ===============\n")



print("==============================wordpunct_tokenize ===============\n")
from nltk.tokenize import wordpunct_tokenize
words_list = wordpunct_tokenize(corpus)
print(words_list)
print("==============================wordpunct_tokenize ===============\n")



print("==============================TreebankWordTokenizer ===============\n")

from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

words_list = tokenizer.tokenize(corpus)

print(words_list)

print("==============================TreebankWordTokenizer ===============\n")
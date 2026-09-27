from pathlib import Path

import nltk

nltk_data_dir = Path(__file__).resolve().parents[2] / "nltk_data"
nltk.data.path.append(str(nltk_data_dir))

try:
    nltk.data.find("corpora/stopwords")
    nltk.data.find("taggers/averaged_perceptron_tagger_eng")
    nltk.data.find("chunkers/maxent_ne_chunker_tab/english_ace_multiclass/")
    nltk.data.find("corpora/words")
except LookupError:
    nltk.download("stopwords", download_dir=str(nltk_data_dir))
    nltk.download("averaged_perceptron_tagger_eng", download_dir=str(nltk_data_dir))
    nltk.download("maxent_ne_chunker_tab", download_dir=str(nltk_data_dir))
    nltk.download("words", download_dir=str(nltk_data_dir))


from nltk.chunk import ne_chunk

sentence="The Eiffel Tower was built from 1887 to 1889 by Gustave Eiffel, whose company specialized in building metal frameworks and structures."

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

list_of_words = word_tokenize(sentence)

post_tag_words_list = []
for word in list_of_words:
    lowerCaseWord = word.lower()
    if lowerCaseWord not in set(stopwords.words('english')):
        post_tag_words_list.append(lowerCaseWord)

tagged_words_list = pos_tag(post_tag_words_list)

ne_chunk(tagged_words_list)
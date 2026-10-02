
# cast tells the editor (Pylance) the real type of a value; it does nothing at runtime
from typing import cast

# gensim's downloader fetches pretrained models/datasets by name
import gensim.downloader as api
# KeyedVectors stores word -> vector mappings and similarity methods
from gensim.models import KeyedVectors

# load Google's pretrained word2vec model (300-dimensional vectors, ~1.6GB download on first run)
wv = cast(KeyedVectors, api.load('word2vec-google-news-300'))

# get the 300-dimensional vector for the word 'king'
vec_king = wv['king']

# print the vector (an array of 300 numbers)
print(vec_king)

# find the top 10 words closest in meaning to 'cricket'
cricket_most_similar = wv.most_similar('cricket')

# print the list of (word, similarity score) pairs
print(cricket_most_similar)

# cosine similarity between 'hockey' and 'sports' (closer to 1 = more similar)
words_similarity = wv.similarity("hockey","sports")

# print the similarity score
print(words_similarity)

# word arithmetic: king - man + woman should land near 'queen'
vec=wv['king']-wv['man']+wv['woman']

# find words closest to the resulting vector
most_similar_vec = wv.most_similar([vec])

# print the closest words (expect 'king' and 'queen' near the top)
print(most_similar_vec)

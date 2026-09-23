
## Classification Problem
## Comments of product is a positive review or negative review
## Reviews----> eating, eat,eaten [going,gone,goes]--->go

words=["eating","eats","eaten","writing","writes","programming","programs","history","finally","finalized"]

print("==============================PorterStemmer ===============\n")

from nltk.stem import PorterStemmer

porterStemmerObj = PorterStemmer()

for word in words:
    print(word+"---->"+porterStemmerObj.stem(word))

print(porterStemmerObj.stem('congratulations'))
print(porterStemmerObj.stem("sitting"))

print("==============================PorterStemmer ===============\n")




print("==============================RegexpStemmer ===============\n")

from nltk.stem import RegexpStemmer

regexpStemmerObj = RegexpStemmer('ing$|s$|e$|able$', min=4)

print(regexpStemmerObj.stem('eating'))
print(regexpStemmerObj.stem('ingeating'))

for word in words:
    print(word+"---->"+regexpStemmerObj.stem(word))

print("==============================RegexpStemmer ===============\n")





print("==============================SnowballStemmer ===============\n")

from nltk.stem import SnowballStemmer

snowballStemmerObj = SnowballStemmer('english')

for word in words:
    print(word+"---->"+snowballStemmerObj.stem(word))

print(porterStemmerObj.stem("fairly") , porterStemmerObj.stem("sportingly"),porterStemmerObj.stem('goes'))

print(snowballStemmerObj.stem("fairly"),snowballStemmerObj.stem("sportingly"),snowballStemmerObj.stem('goes'))

print("==============================SnowballStemmer ===============\n")
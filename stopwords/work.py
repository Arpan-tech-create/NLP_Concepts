import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

data="Hello, i'm arpan bhoi from gujarat. do you have any query about my presentation"

stop_words=set(stopwords.words('english'))

print(stopwords.words() [620:680])

#-------------------------tokenization-----------------------#
token=nltk.word_tokenize(data)
print("TOKENIZATION : ",token)
#---------------------------------------------#

#------------------what are the stopwords in my data--------------#
print("Stopwords are as follows...............")
for word in data:
    if word in stop_words:
        
        print(word)


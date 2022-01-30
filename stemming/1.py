import nltk

from  nltk.stem import PorterStemmer

portstem=PorterStemmer()
words=["Give","Giving","Gives","Given"]

for i in words:
    print(i,":",portstem.stem(i))
    
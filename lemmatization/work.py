import nltk
from nltk.stem import WordNetLemmatizer

lemmet=WordNetLemmatizer()

print("mice",lemmet.lemmatize("mice"))

print("loaves",lemmet.lemmatize("loaves"))
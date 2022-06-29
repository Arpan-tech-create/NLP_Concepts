import nltk

data="Hello im arpan bhoi . aap kese ho. good ne!!!!!!"

tokens=nltk.sent_tokenize(data)

print(tokens)
print(type(tokens))
print(len(tokens))

#------------------------------------------------#


print("Now word tokenization..................")

tokens1=nltk.word_tokenize(data)
print(tokens1)
print(type(tokens1))
print(len(tokens1))
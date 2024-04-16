import streamlit as st
import nltk
import spacy
import pandas as pd
import nltk
from nltk import FreqDist
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import RegexpTokenizer
import matplotlib.pyplot as plt

#read the csv
data= pd.read_csv("C:/Users/saisr/OneDrive/Desktop/3rd sem/Adv Python/ESE/WomensClothingE-CommerceReviews.csv")
#convert the csv into text
text = data.to_string(index=False)


st.title("Text Analysis")
st.subheader("Pre Processing")
st.write("")
token1=sent_tokenize(text)
len(token1)
my_string = ' '.join(map(str, token1))

#stop words
import regex as re
clean=re.sub(r'[^\w\s]', '', my_string)
print(len(clean))

from nltk.corpus import stopwords
given_text=word_tokenize(clean)
stop_words= set(stopwords.words("english"))
filtered_list=[]
for word in given_text:
    if word.casefold() not in stop_words:
        filtered_list.append(word)

print(filtered_list)
# print(len(filtered_list))


from nltk.stem import PorterStemmer
stemmer= PorterStemmer()
stemmed_words=[stemmer.stem(word) for word in filtered_list]
# print(stemmed_words)
print(len(stemmed_words))


from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
my_string1 = ' '.join(map(str, stemmed_words))
lemmatizer.lemmatize(my_string1)

final =WordPunctTokenizer().tokenize(my_string)

fd= nltk.FreqDist(stemmed_words)
f1= fd.most_common(20)
print(f1)


def preprocess_text(text1):
    words=sent_tokenize(text1)
    given_text1=word_tokenize(text1)
    stop_words= set(stopwords.words("english"))
    filtered_list=[]
    for word in given_text1:
        if word.casefold() not in stop_words:
            filtered_list.append(word)
    stemmer= PorterStemmer()
    stemmed_words=[stemmer.stem(word) for word in filtered_list]
    return text1

def jaccard_similarity(set1,set2):
    intersection= len(set1.intersection(set2))
    union= len(set1.union(set2))
    return intersection/union

token1=set(preprocess_text(text))
similarity_score= jaccard_similarity(token1)
print(f"jaccard similarity: {similarity_score}")

vectorizer = TfidfVectorizer()
vector1= vectorizer.fit_transform([text])

cosine_similarity_score = cosine_similarity(vector1)
print(f"Cosine Similarity Score: {cosine_similarity_score}")





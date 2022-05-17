#generate corpus 
import sys
import os
sys.path.append(".")
sys.path.append("./")
import pandas as pd
from src.db.Database import DB
import re
import pickle
import nltk
import pandas as pd
import sqlite3
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from nltk.tokenize.toktok import ToktokTokenizer


nltk.download('stopwords')
stopword_list=nltk.corpus.stopwords.words('english')
tokenizer=ToktokTokenizer()


def clean_sentence(sentence):
    sentence=sentence.lower().strip()
    sentence=re.sub(r'[^a-zA-Z0-9]',' ',sentence)
    return sentence
def get_clean_sentence(sentence):
    sentence=clean_sentence(sentence)
    return sentence

def simpler_stemmer(sentence):
    ps=nltk.porter.PorterStemmer()
    sentence=' '.join([ps.stem(word) for word in sentence.split()])
    return sentence


def remove_stopwords(sentence,is_lower_case=False):
    tokens=tokenizer.tokenize(sentence)
    tokens=[token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens=[token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens=[token.lower() for token in tokens if token.lower() not in stopword_list]
    filtered_sentence=' '.join(filtered_tokens)
    return filtered_sentence
def create_corpa():
    con = sqlite3.connect("src\\db\\app.db")
    df = pd.read_sql_query("SELECT * from functions LIMIT 100;", con)
    df['Command']=df['Command'].apply(get_clean_sentence)
    df['Command']=df['Command'].apply(remove_stopwords)
    df['Command']=df['Command'].apply(simpler_stemmer)
    tfidf=CountVectorizer()
    tfidf_df=tfidf.fit_transform(df['Command'])
    tfidf_df = tfidf_df.toarray()
    with open("src/tokens", 'wb') as fout:
        pickle.dump((df, tfidf_df, tfidf), fout)


def sentence_pipeline(sentence,model,corpa):
    sentence = get_clean_sentence(sentence)
    sentence = remove_stopwords(sentence)
    sentence = simpler_stemmer(sentence)
    sentence = model.transform([sentence])
    sentence = sentence.toarray()
    result = cosine_similarity(sentence,corpa)
    return np.argmax(result)
if __name__ == '__main__':
    create_corpa()
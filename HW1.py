import re
import nltk
import numpy as np
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer

#nltk.download('punkt')
#nltk.download('wordnet')

namelist = ["doc1.txt", "doc2.txt", "doc3.txt", "doc4.txt", "doc5.txt"]

wordnet_lemmatizer = WordNetLemmatizer()
porter_stemmer = PorterStemmer()


def read_document(name):
    with open(name, "r") as f:
        document = f.read()
    return document

def remove_punctuation(document):
    #\w means we match normal letters
    #\s means we match blank
    document = re.sub(r'[^\w\s]', '', document)
    #remove leading and trailing space
    return document.strip()

def case_folding(document):
    return document.lower()

def tokenize(document):
    #return [i for i in re.findall('\w+', document)]
    return nltk.word_tokenize(document)

def remove_stop_words(token):
    stop_words = open('stop_words.txt').read().split('\n')
    return [i for i in token if i not in stop_words]

def lemmatization(token):
    return [wordnet_lemmatizer.lemmatize(i) for i in token]

def stemming(token):
    return [porter_stemmer.stem(i) for i in token]

def preprocess(filename):
    doc = read_document(filename)

    doc = remove_punctuation(doc)

    doc = case_folding(doc)
    token = tokenize(doc)
    token = remove_stop_words(token)

    token = lemmatization(token)
    token = stemming(token)
    return token

def calculate_term_document_matrix(namelist):
    corpus = {}

    tokens = []
    for name in namelist:
        token = preprocess(name)
        corpus[name] = token
        tokens.extend(token)
    tokens = list(set(tokens))
    tokens.sort()

    matrix = {}
    for token in tokens:
        matrix[token] = []
        for name in namelist:
            if(token in corpus[name]):
                matrix[token].append(1)
            else:
                matrix[token].append(0)
    return tokens, corpus, matrix

def calculate_tf_idf(tokens, corpus, matrix):
    #calculate tf
    tf = np.zeros((len(corpus), len(tokens)))
    i = 0
    for doc in corpus.values():
        for word in doc:
            tf[i][tokens.index(word)] += 1
        tf[i] /= len(doc)
        i += 1

    #calculate idf
    idf = np.zeros(len(tokens))
    for i in range(len(tokens)):
        nums_of_appearance = np.array(matrix[tokens[i]]).sum()
        idf[i] = np.log(len(corpus)/nums_of_appearance)

    tf_idf = np.multiply(tf,idf)
    return tf_idf

def calculate_cosine_similarity(tf_idf, doc_num):
    similarity_matrix = np.zeros((doc_num,doc_num))

    for i in range(doc_num):
        for j in range(i,doc_num):
            modi = np.sqrt(np.dot(tf_idf[i],tf_idf[i]))
            modj = np.sqrt(np.dot(tf_idf[j],tf_idf[j]))
            similarity_matrix[i][j] = np.dot(tf_idf[i], tf_idf[j])/(modi * modj)

    return similarity_matrix


#Task1
for name in namelist:
    doc = preprocess(name)
    print(doc)

#Task2
tokens, corpus, matrix = calculate_term_document_matrix(namelist)
#print(tokens)
#print(corpus)
print("term document matrix is:")
print(matrix)

#Task3
tf_idf = calculate_tf_idf(tokens, corpus, matrix)
print("tf_idf matrix is:")
print(tf_idf)

#Task4
similarity_matrix = calculate_cosine_similarity(tf_idf, len(corpus))
print("similarity matrix is:")
print(similarity_matrix)






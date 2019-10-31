import spacy 

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

nlp = spacy.load('en_core_web_lg')

df=pd.read_excel("Chatbot.xlsx")

queries=np.array(df['text'])
labels=np.array(df['intent'])


# spacy NLP Model
nlp = spacy.load('en_core_web_lg')
# Calculate the length of sentences

n_queries=len(queries)
dim_embedding = nlp.vocab.vectors_length
X = np.zeros((n_queries, dim_embedding))



for idx, sentence in enumerate(queries):
    doc = nlp(sentence)
    X[idx, :] = doc.vector

X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.30, random_state=42)

print("Train X: ",X_train.shape)
print("Train y: ",y_train.shape)
print("Text X: ",X_test.shape)
print("Test y: ",y_test.shape)


neigh = KNeighborsClassifier(n_neighbors=1)

neigh.fit(X_train,y_train)

print("Accuracy on Test Set: ",np.count_nonzero(neigh.predict(X_test)==y_test)/len(y_test))

doc = nlp('from olympia einkaufszentrum to hauptbahnhof')

neigh.predict(doc.vector.reshape(1,-1))

##Entity Extractor using Spacy
for ent in doc.ents:
    print(ent.text,ent.label_)
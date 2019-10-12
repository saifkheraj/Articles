import wikipedia
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.metrics.pairwise import cosine_similarity


articles=['Data Mining','Machine Learning','Cricket','Swimming','Tennis']
wiki_lst=[]

for article in articles:
    print(article)
    wiki_lst.append(wikipedia.page(article).content)


cv = CountVectorizer()
X=cv.fit_transform(wiki_lst)


print("Data Mining and Machine Learning",euclidean_distances(X[0],X[1]))
print("Data Mining and Cricket",euclidean_distances(X[0],X[2]))
print("Data Mining and Swimming",euclidean_distances(X[0],X[3]))
print("Data Mining and Tennis",euclidean_distances(X[0],X[4]))

print("Data Mining and Machine Learning",cosine_similarity(X[0],X[1]))
print("Data Mining and Cricket",cosine_similarity(X[0],X[2]))
print("Data Mining and Swimming",cosine_similarity(X[0],X[3]))
print("Data Mining and Tennis",cosine_similarity(X[0],X[4]))

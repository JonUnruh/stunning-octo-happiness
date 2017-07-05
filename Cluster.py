from sklearn import cluster
import pandas as pd
from matplotlib import pyplot
import numpy as np

df = pd.read_csv('amelec-hashtag.csv', sep=';', encoding = 'latin-1')
arr = df['Inhalt'].str.len()
arr = np.array(arr)
data = arr.reshape(-1, 1)
yoho = np.zeros(shape=(225625,1))
count = 0
for x in data:
    for y in data:
        yoho[count] = abs(x - y)
        count = count +1

rum = np.zeros(shape=(225625,1))

def distance(first, second):
    if len(first) > len(second):
        first, second = second, first
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [[0] * second_length for x in range(first_length)]
    for i in range(first_length):
        distance_matrix[i][0] = i
    for j in range(second_length):
        distance_matrix[0][j]=j
    for i in range(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i-1][j] + 1
            insertion = distance_matrix[i][j-1] + 1
            substitution = distance_matrix[i-1][j-1]
            if first[i-1] != second[j-1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    return distance_matrix[first_length-1][second_length-1]

count = 0
for x in df['Inhalt']:
    for y in df['Inhalt']:
        rum[count] = distance(x, y)
        count = count +1

data = np.concatenate((yoho, rum), axis = 1)

k = 3
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(data)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_
for i in range(k):
    ds = data[np.where(labels==i)]
    pyplot.plot(ds[:,0],ds[:,1],'o')
    lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
    pyplot.setp(lines,ms=15.0)
    pyplot.setp(lines,mew=2.0)
pyplot.show()


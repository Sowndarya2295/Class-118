import pandas as pd
import plotly.express as px
df = pd.read_csv("petals_sepals.csv")
print(df.head())
fig = px.scatter(df, x="petal_size", y="sepal_size")
fig.show()

from sklearn.cluster import KMeans
X = df.iloc[:, [0, 1]].values
print(X)
wcss = []


for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 42)

kmeans.fit(X)

 
wcss.append(kmeans.inertia_)
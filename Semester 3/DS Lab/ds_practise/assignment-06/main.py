# Assignment 6: K-Means Clustering on Tissue Gene Expression Dataset

from sklearn.datasets import fetch_openml
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

# Load tissue_gene_expression dataset from OpenML
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer(as_frame=True)
X = data.data
y = data.target

# Run K-Means with K = 7
kmeans = KMeans(n_clusters=7, random_state=42, n_init=10)
clusters = kmeans.fit_predict(X)

# Compare clusters with actual tissue types
comparison = pd.crosstab(y, clusters)
print("Cluster vs Tissue Type Comparison Table:\n")
print(comparison)

# Run several times to observe changes
for i in range(3):
    kmeans = KMeans(n_clusters=7, random_state=None, n_init=10)
    clusters = kmeans.fit_predict(X)
    print(f"\nRun {i+1} - Cluster vs Tissue Type Comparison:\n")
    print(pd.crosstab(y, clusters))

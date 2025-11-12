# --- File: 2_run_kmeans.py (Corrected) ---

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder  # <-- IMPORT THIS
import numpy as np

# --- 1. Load and Prepare the Data ---
try:
    df = pd.read_csv('tissue_gene_expression.csv')
except FileNotFoundError:
    print("Error: 'tissue_gene_expression.csv' not found.")
    print("Please run the first script (1_get_data.py) to create this file.")
    exit()

print("Data loaded successfully.")

# --- 2. Preprocess the Data ---
X = df.drop('tissue_type', axis=1)
y_true_strings = df['tissue_type']

le = LabelEncoder()
y_true_encoded = le.fit_transform(y_true_strings)

tissue_labels = le.classes_

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# --- 3. Run K-Means (First Run) ---
print("\n--- Running K-Means (Run 1) with K=7 and random_state=42 ---")

kmeans_1 = KMeans(n_clusters=7, random_state=42, n_init=10)
y_pred_1 = kmeans_1.fit_predict(X_scaled)

# --- 4. Create the Comparison Table ---
cm_1 = confusion_matrix(y_true_encoded, y_pred_1)

cm_df_1 = pd.DataFrame(cm_1,
                       index=[f"True: {label}" for label in tissue_labels],
                       columns=[f"Cluster: {i}" for i in range(7)])

print("\nComparison Table (Run 1):")
print(cm_df_1)

# --- 5. Visualize the Comparison Table ---
plt.figure(figsize=(10, 7))
sns.heatmap(cm_df_1, annot=True, fmt='d', cmap='viridis', linewidths=.5)
plt.title('Run 1: True Tissue Type vs. K-Means Cluster')
plt.ylabel('Actual Tissue Type')
plt.xlabel('Predicted Cluster Label')
plt.tight_layout()
plt.show()

# --- 6. Run K-Means Several Times (Second Run) ---
print("\n--- Running K-Means (Run 2) with K=7 and random_state=101 ---")

kmeans_2 = KMeans(n_clusters=7, random_state=101, n_init=10)
y_pred_2 = kmeans_2.fit_predict(X_scaled)

cm_2 = confusion_matrix(y_true_encoded, y_pred_2)
cm_df_2 = pd.DataFrame(cm_2,
                       index=[f"True: {label}" for label in tissue_labels],
                       columns=[f"Cluster: {i}" for i in range(7)])

print("\nComparison Table (Run 2):")
print(cm_df_2)

"""
--- Observation on Variability ---
Compare the two tables. You will notice the cluster labels (columns) are permuted
For example, in Run 1, 'cerebellum' might map mostly to 'Cluster 2'
In Run 2, it might map to 'Cluster 5'
This happens because the cluster labels (0, 1, 2...) are just arbitrary numbers,
and the final assignment depends on the *random* initial placement of centroids
"""
# Data Science Assignment 9
# Topic: Market Basket Analysis using FP-Growth Algorithm

# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules

# -----------------------------
# Step 1: Create Sample Retail Dataset
# -----------------------------
dataset = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter', 'jam'],
    ['milk', 'bread'],
    ['milk', 'bread', 'butter', 'jam'],
    ['bread', 'butter']
]

# Convert dataset into one-hot encoded DataFrame
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

print("=== Transaction Dataset ===")
print(df)

# -----------------------------
# Step 2: Apply FP-Growth Algorithm
# -----------------------------
frequent_itemsets = fpgrowth(df, min_support=0.4, use_colnames=True)
print("\n=== Frequent Itemsets ===")
print(frequent_itemsets)

# -----------------------------
# Step 3: Generate Association Rules
# -----------------------------
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
print("\n=== Association Rules ===")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# -----------------------------
# Step 4: Interpretation
# -----------------------------
print("\n=== Insights ===")
print("1. Items frequently bought together are identified.")
print("2. High confidence and lift values suggest strong relationships between items.")
print("3. Retailers can use these insights to create combo offers or product placements.")

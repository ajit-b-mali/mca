# Assignment 7: Frequent Pattern Tree (FP-Growth) on Grocery Dataset

from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

# Sample grocery transactions (you can expand as needed)
dataset = [
    ['milk', 'bread', 'eggs'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['bread', 'butter', 'jam'],
    ['milk', 'bread', 'butter'],
]

# Encode dataset for FP-Growth
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Build FP-Tree using FP-Growth
frequent_itemsets = fpgrowth(df, min_support=0.001, use_colnames=True)
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)

print("Frequent Itemsets:\n", frequent_itemsets)
print("\nAssociation Rules (confidence ≥ 0.8):\n", rules[['antecedents', 'consequents', 'support', 'confidence']])

# Show how transactions evolve (conceptually)
print("\nTree Evolution per Transaction:")
for i, t in enumerate(dataset, 1):
    print(f"After Transaction {i}: {t} added to FP-Tree structure.")

# Assignment 8: Apriori Algorithm on Grocery Dataset

from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pandas as pd

# Sample grocery dataset
dataset = [
    ['milk', 'bread', 'eggs'],
    ['bread', 'butter'],
    ['milk', 'bread', 'butter', 'eggs'],
    ['bread', 'butter', 'jam'],
    ['milk', 'bread', 'butter'],
]

# Encode dataset
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.001, use_colnames=True)

# Generate association rules
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)

# Sort by confidence
rules = rules.sort_values(by='confidence', ascending=False)

# Display top 5 rules
top5 = rules.head(5)
print("Top 5 Association Rules (Sorted by Confidence):\n")
print(top5[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# Highlight strong rules (confidence ≥ 0.9)
strong_rules = top5[top5['confidence'] >= 0.9]
print("\nStrong Association Rules (confidence ≥ 0.9):\n")
print(strong_rules[['antecedents', 'consequents', 'confidence', 'lift']])

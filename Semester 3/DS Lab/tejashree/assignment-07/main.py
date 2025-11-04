import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth, association_rules
from tabulate import tabulate

filename = 'groceries.csv'
dataset = []

try:
    df = pd.read_csv(filename)
    df = df.drop(columns=df.columns[0])
    for index, row in df.iterrows():
        transaction = row.dropna().tolist()
        dataset.append(transaction)

except FileNotFoundError:
    print(f"Error: '{filename}' not found. Please make sure the file is in the same directory as the script.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

min_support_threshold = 0.01 # in assignment 0.001
frequent_itemsets = fpgrowth(df_encoded, min_support=min_support_threshold, use_colnames=True)

min_confidence_threshold = 0.5 # in assignment 0.8
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence_threshold)

print("\n" + "="*80)
print(" " * 20 + "FP-GROWTH ANALYSIS RESULTS")
print("="*80 + "\n")

print(f"📊 Top 10 Frequent Itemsets (Support >= {min_support_threshold})")
sorted_itemsets = frequent_itemsets.sort_values(by='support', ascending=False)
print(tabulate(sorted_itemsets.head(10), headers='keys', tablefmt='psql', showindex=False))
print(f"\n[INFO] Found a total of {len(frequent_itemsets)} frequent itemsets.\n")

print(f"🔗 Generated Association Rules (Confidence >= {min_confidence_threshold})")
if rules.empty:
    print("No rules found for the given support and confidence thresholds.")
else:
    relevant_rules = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]
    sorted_rules = relevant_rules.sort_values(by=['confidence', 'lift'], ascending=False)
    print(tabulate(sorted_rules.head(10), headers='keys', tablefmt='psql', showindex=False, floatfmt=".4f"))
print(f"\n[INFO] Found a total of {len(rules)} rules.\n")
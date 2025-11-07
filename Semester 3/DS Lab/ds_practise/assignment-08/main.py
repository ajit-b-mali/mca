# --- Step 1: Import necessary libraries ---
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder


# --- Step 2: Data Loading and Preparation ---
filename = 'groceries.csv'
dataset = []
try:
    df = pd.read_csv(filename)

    # Drop the first column ("Item(s)") as it's just a count, not an item
    df = df.drop(columns=df.columns[0])

    # Convert each row into a transaction list, automatically ignoring empty cells (NaNs)
    for index, row in df.iterrows():
        transaction = row.dropna().tolist()
        dataset.append(transaction)

except FileNotFoundError:
    print(f"Error: '{filename}' not found. Please make sure the file is in the same directory as the script.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

# One-Hot Encode the Data for mlxtend
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)


# --- Step 3: Apply the Apriori algorithm with your specified support ---
min_support_threshold = 0.001
frequent_itemsets = apriori(df_encoded, min_support=min_support_threshold, use_colnames=True)
print(f"\nFound {len(frequent_itemsets)} frequent itemsets with support >= {min_support_threshold}.")


# --- Step 4: Generate association rules with your specified confidence ---
min_confidence_threshold = 0.8
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence_threshold)

# --- Step 5: Sort the rules and display the top 5 ---
rules_sorted = rules.sort_values(by='confidence', ascending=False)
print("\n--- Top 5 Association Rules (sorted by confidence) ---")
print(rules_sorted.head(5))
if rules.empty:
    print("No rules found for the given support and confidence thresholds.")

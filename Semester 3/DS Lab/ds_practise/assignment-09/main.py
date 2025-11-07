import pandas as pd
from mlxtend.frequent_patterns import fpgrowth, association_rules
from mlxtend.preprocessing import TransactionEncoder

try:
    df = pd.read_csv('groceries.csv').drop(columns=['Item(s)'])
    print("✅ Dataset loaded successfully!")
except FileNotFoundError:
    print("❌ Error: 'groceries.csv' not found. Please save the data to a file first.")
    exit()

transactions = []
for index, row in df.iterrows():
    basket = row.dropna().tolist()
    transactions.append(basket)

print(f"\nSuccessfully created {len(transactions)} transaction baskets.")
print("Example basket:", transactions[0])

te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df_encoded = pd.DataFrame(te_ary, columns=te.columns_)

frequent_itemsets = fpgrowth(df_encoded, min_support=0.005, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.1)

print("\n--- Top 10 Association Rules (sorted by Lift) ---")
if rules.empty:
    print("No association rules found. Try lowering the 'min_support' or 'min_confidence' values.")
else:
    rules_sorted = rules.sort_values(by='lift', ascending=False)
    print(rules_sorted.head(10)[['antecedents', 'consequents', 'support', 'confidence', 'lift']])

# --- 6. How to Interpret the Results ---
# - antecedents: The item(s) a customer buys.
# - consequents: The item(s) the customer is likely to buy in addition.
# - support: How often the items are bought together.
# - confidence: The probability of buying 'consequents' if 'antecedents' are already in the cart.
# - lift: A value greater than 1 indicates a positive relationship,
#         meaning the items are more likely to be bought together than by random chance.


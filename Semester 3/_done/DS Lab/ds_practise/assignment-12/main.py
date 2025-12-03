import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. Load the Dataset ---
try:
    mtcars_data = sm.datasets.get_rdataset("mtcars", "datasets")
    df = mtcars_data.data
    print("Successfully loaded the 'mtcars' dataset.")
except Exception as e:
    print(f"Failed to load dataset. Error: {e}")
    exit()

# --- 2. Create the Boxplot ---
sns.set_style("whitegrid")
plt.figure(figsize=(8, 6))
sns.boxplot(x='cyl', y='mpg', data=df, palette='viridis')

# --- 3. Customize the Plot ---
plt.title('Boxplot of MPG by Number of Cylinders')
plt.xlabel('Number of Cylinders (cyl)')
plt.ylabel('Miles Per Gallon (mpg)')

# --- 4. Save and Show the Plot ---
plt.savefig('mtcars_mpg_vs_cyl_boxplot.png')
plt.show()

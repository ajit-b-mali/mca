# Assignment 11: Create and Save a Bar Chart of Movie Scores

import pandas as pd
import matplotlib.pyplot as plt

# --- 1. Read the CSV File ---
try:
    # Read the data from the CSV file into a pandas DataFrame
    df = pd.read_csv('moviesData.csv')
    print("✅ 'moviesData.csv' loaded successfully.")
except FileNotFoundError:
    print("❌ Error: 'moviesData.csv' not found. Please make sure the file is in the same directory.")
    exit()

# --- 2. Select the First 10 Movies ---
# Use the .head() method to get the first 10 rows of the DataFrame
first_10_movies = df.head(10)

# --- 3. Create the Bar Chart ---
# Create a figure and axes for the plot to have more control over its size
plt.figure(figsize=(12, 7))

# Create the bar chart
# X-axis: Movie titles
# Y-axis: Critics' scores
plt.bar(first_10_movies['title'], first_10_movies['critics_score'], color='skyblue')

# --- 4. Customize the Plot ---
plt.xlabel("Movie Title", fontsize=12)
plt.ylabel("Critics' Score", fontsize=12)
plt.title("Critics' Score for the First 10 Movies", fontsize=16)

# Rotate the x-axis labels (movie titles) to prevent them from overlapping
plt.xticks(rotation=45, ha='right')

# Add a grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to make sure everything fits without being cut off
plt.tight_layout()

# --- 5. Save the Plot to a File ---
try:
    output_filename = 'critics_score_barchart.png'
    plt.savefig(output_filename)
    print(f"✅ Chart successfully saved as '{output_filename}'")
except Exception as e:
    print(f"❌ Error saving the file: {e}")

# --- 6. Display the Plot ---
# This will show the plot in a new window when you run the script
plt.show()

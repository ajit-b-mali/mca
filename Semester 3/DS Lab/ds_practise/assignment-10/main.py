# Assignment 10: Create a Stacked Bar Chart in Python

import matplotlib.pyplot as plt
import numpy as np

# --- 1. Define the data and parameters ---

# Given colors for the regions
colors = ["green", "orange", "brown"]

# Given months for the X-axis
months = ["Mar", "Apr", "May", "Jun", "Jul"]

# Given regions for the legend and data series
regions = ["East", "West", "North"]

# Create a NumPy array of the revenue data (in thousands)
# Each row corresponds to a region, and each column to a month.
revenue_data = np.array([
  # East Region Revenue
  [20, 35, 30, 35, 27],
  # West Region Revenue
  [25, 28, 29, 31, 33],
  # North Region Revenue
  [40, 23, 38, 33, 45]
])

# --- 2. Create the Stacked Bar Chart ---

# Get the number of months and regions
num_months = len(months)
num_regions = len(regions)

# The bottom values for each stack. Starts at zero.
bottom = np.zeros(num_months)

# Create a figure and axis object for the plot
fig, ax = plt.subplots(figsize=(10, 6))

# Loop through each region to plot its data as a layer in the stack
for i in range(num_regions):
    ax.bar(
        months,                      # X-axis values
        revenue_data[i],             # Heights for this region's bars
        bottom=bottom,               # Where this stack starts from
        label=regions[i],            # Label for the legend
        color=colors[i],             # Color for this stack
        edgecolor="white"            # Add a white border for separation
    )
    # Add the current region's revenue to the bottom for the next stack
    bottom += revenue_data[i]

# --- 3. Customize and Display the Plot ---

ax.set_xlabel("Month", fontsize=12)
ax.set_ylabel("Revenue (in thousands)", fontsize=12)
ax.set_title("Monthly Revenue by Region", fontsize=16)
ax.legend(title="Regions") # Add the legend with a title

# Ensure the layout is tight and display the plot
plt.tight_layout()
plt.show()

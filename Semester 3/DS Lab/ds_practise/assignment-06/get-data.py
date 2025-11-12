# --- File: 1_get-data.py (Final Context-Managed Version) ---

import pandas as pd
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
from rpy2.robjects import pandas2ri
from rpy2.robjects import conversion as rpy2_conversion
from rpy2.rinterface_lib.embedded import RRuntimeError

print("Setting up rpy2...")

# Create the converter template we'll use later
pandas_converter = rpy2_conversion.Converter('pandas_converter', template=pandas2ri.converter)

try:
    # --- R-ONLY OPERATIONS (No conversion context) ---
    
    # Import R's 'utils' package
    utils = importr('utils')

    # Select a CRAN mirror
    print("Selecting CRAN mirror...")
    utils.chooseCRANmirror(ind=1)

    # Try to import dslabs.
    try:
        dslabs = importr('dslabs')
        print("'dslabs' package already installed.")
    except Exception: 
        print("Could not import 'dslabs', attempting installation...")
        utils.install_packages('dslabs')
        dslabs = importr('dslabs')
        print("Installation complete.")

    # Load the dataset in R's environment
    print("Loading 'tissue_gene_expression' dataset...")
    ro.r('data(tissue_gene_expression)')

    # Get handles to the raw R objects
    print("Getting R object handles...")
    r_data = ro.r['tissue_gene_expression']
    r_matrix = r_data[0]
    r_vector = r_data[1]
    
    # Call R's 'colnames' function using the R matrix handle
    # The result is still an R object (a vector of strings)
    print("Fetching column names (as R object)...")
    r_colnames = ro.r['colnames'](r_matrix)

    # --- PYTHON CONVERSION OPERATIONS ---
    
    # Now, use the modern 'localconverter' context to convert
    # all the R objects we've gathered into Python objects.
    print("Converting R objects to Python objects...")
    with rpy2_conversion.localconverter(ro.default_converter + pandas_converter):
        
        # Convert the R matrix to a NumPy array
        gene_expression_numpy = ro.conversion.rpy2py(r_matrix)
        
        # Convert the R factor (vector) to a NumPy array
        tissue_types_numpy = ro.conversion.rpy2py(r_vector)
        
        # Convert the R string vector to a Python list
        gene_column_names = list(ro.conversion.rpy2py(r_colnames))

    # --- PANDAS-ONLY OPERATIONS ---
    
    print("Building pandas DataFrame from Python objects...")
    
    # We now use standard pandas to build the DataFrame.
    gene_expression_df = pd.DataFrame(
        data=gene_expression_numpy,
        columns=gene_column_names
    )
    
    # Add the tissue type column
    gene_expression_df['tissue_type'] = tissue_types_numpy

    # Save to a CSV file
    output_filename = 'tissue_gene_expression.csv'
    gene_expression_df.to_csv(output_filename, index=False)

    print(f"\nSuccessfully saved data to '{output_filename}'")
    print("\nDataFrame head:")
    print(gene_expression_df.head())

except RRuntimeError as e:
    print(f"\n--- AN R RUNTIME ERROR OCCURRED ---")
    print(f"Error: {e}")

except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
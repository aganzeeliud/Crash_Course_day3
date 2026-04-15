import pandas as pd

# 1. Load the Excel file
# Pandas is like Excel but for programming. It helps us work with tables.
print("Loading floodarchive.xlsx...")
df = pd.read_excel('floodarchive.xlsx', engine='openpyxl')

# 2. Filter the rows
# We search for rows where the 'Country' is 'DR Congo'.
# To be safe, we also include other common names for the same country 
# that we found in the file, like 'Democratic Republic of Congo'.
variations = ['DR Congo', 'Democratic Republic of Congo', 'Democratic Republic Congo']

# This code says: "Keep rows where the Country name contains any of our variations"
filtered_df = df[df['Country'].str.contains('|'.join(variations), case=False, na=False)]

# 3. Save the result
# We save the results into a new file called 'dr_congo_floods.csv'.
# CSV files are simple text files that are easy to share and open in Excel.
output_file = 'dr_congo_floods.csv'
filtered_df.to_csv(output_file, index=False)

print(f"Done! Found {len(filtered_df)} rows for DR Congo.")
print(f"The result has been saved to: {output_file}")

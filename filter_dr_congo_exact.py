import pandas as pd

# 1. Load the Excel file
# We use pandas to open the 'floodarchive.xlsx' file.
print("Loading floodarchive.xlsx...")
df = pd.read_excel('floodarchive.xlsx', engine='openpyxl')

# 2. Filter for the specific name
# We are looking for the exact spelling: "Democratic  Republic of the Congo"
# Notice the two spaces between 'Democratic' and 'Republic'!
target_name = "Democratic  Republic of the Congo"
filtered_df = df[df['Country'] == target_name]

# 3. Save to a new CSV file
# We save only these rows into a file named 'dr_congo_specific.csv'.
output_file = 'dr_congo_specific.csv'
filtered_df.to_csv(output_file, index=False)

print(f"Done! Found {len(filtered_df)} rows for '{target_name}'.")
print(f"The result has been saved to: {output_file}")

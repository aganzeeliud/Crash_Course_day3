import pandas as pd

# Step 1: Read the Excel file
# We use a library called 'pandas' which is great for working with data tables.
# 'read_excel' is the command that opens our 'floodarchive.xlsx' file.
df = pd.read_excel('floodarchive.xlsx')

# Step 2: Define the country we are looking for
# We need to match the name exactly, including spaces.
# The user specified 'Democratic  Republic of the Congo' (note the two spaces).
target_country = "Democratic  Republic of the Congo"

# Step 3: Filter the data
# We tell pandas to keep only the rows where the 'Country' column is our target.
filtered_data = df[df['Country'] == target_country]

# Step 4: Save the result to a CSV file
# We save this filtered list into a new file called 'dr_congo_result.csv'.
# 'index=False' prevents pandas from adding an extra column of row numbers.
filtered_data.to_csv('dr_congo_result.csv', index=False)

# Step 5: Print a success message
print(f"Filter complete! Found {len(filtered_data)} matching rows.")
print("The result has been saved to 'dr_congo_result.csv'.")

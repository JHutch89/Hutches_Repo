import pandas as pd
import json
import urllib.parse

file_path = '/Users/jasonhutches/Desktop/Jason Hutches/Book1.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)


# Define the function to extract IDs
def extract_ids(query_map_str):
    # Step 1: Remove 'pr:"' prefix and the trailing double quote
    json_str = query_map_str[4:-1]  # Adjust indices as needed based on your data
    
    # Step 2: URL decode
    decoded_json_str = urllib.parse.unquote(json_str)
    
    # Step 3: Parse JSON
    try:
        json_obj = json.loads(decoded_json_str)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return []  # Return an empty list or handle as needed
    
    # Step 4: Extract IDs
    ids = [item["id"] for item in json_obj.values()]
    
    return ids

# Assuming you have a DataFrame `df` with a column `query_map` containing your data
# Apply the function to each row in the DataFrame and store the result in a new column
df['extracted_ids'] = df['query_map'].apply(extract_ids)

# Check the result
print(df[['query_map', 'extracted_ids']])

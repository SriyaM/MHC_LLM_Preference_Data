import pandas as pd
import json

# Load the mapping JSON file
with open("mapping.json", "r") as file:  # Path retained as-is
    mapping = json.load(file)

# Load the raw data
raw_data = pd.read_csv("../data/raw/pref_data_raw.csv")  # Input file retained as-is

# Create a copy of the raw data to modify
processed_data = raw_data.copy()

# Normalize column names in the dataset
processed_data.columns = processed_data.columns.str.strip().str.lower()

# Convert all numeric column values to strings
def convert_to_string(value):
    if pd.isnull(value):  # Leave NaN as is
        return value
    return str(int(value)) if isinstance(value, (int, float)) else str(value).strip()

# Handle multiple ethnicities
def process_ethnicity(value):
    if pd.isnull(value):  # Leave NaN as is
        return value
    values = str(value).split(",")  # Split multiple values
    mapped_values = [mapping["Ethnicity"]["mapping"].get(v.strip(), v) for v in values]
    return ", ".join(mapped_values)  # Rejoin after mapping

# Apply mappings to relevant columns
for column, info in mapping.items():
    # Handle columns with direct mappings
    if "mapping" in info and "applicable_columns" not in info:
        col_name = column.lower().strip()
        if col_name in processed_data.columns:
            if col_name == "ethnicity":  # Special case for ethnicity
                processed_data[col_name] = processed_data[col_name].apply(process_ethnicity)
            else:
                processed_data[col_name] = processed_data[col_name].apply(convert_to_string).map(info["mapping"]).fillna(processed_data[col_name])
    # Handle multiple columns for message preferences
    elif "applicable_columns" in info and column == "Message_Preferences":
        for msg_column in info["applicable_columns"]:
            if msg_column in processed_data.columns:
                processed_data[msg_column] = processed_data[msg_column].apply(convert_to_string).map(info["mapping"]).fillna(processed_data[msg_column])

# Save the processed data to a new CSV
processed_data.to_csv("../data/processed/pref_data_processed.csv", index=False)  # Output file retained as-is

print("Processed data has been saved to pref_data_processed.csv")

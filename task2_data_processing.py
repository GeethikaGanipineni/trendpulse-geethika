import pandas as pd
import json
import os

# Step 1: Find latest JSON file inside data folder
data_folder = "data"

files = os.listdir(data_folder)
json_files = [f for f in files if f.endswith(".json")]

if not json_files:
    print("No JSON files found")
    exit()

# Take latest file
json_files.sort()
latest_file = json_files[-1]

file_path = os.path.join(data_folder, latest_file)

print("Using file:", file_path)

# Step 2: Load JSON data
with open(file_path, "r") as f:
    data = json.load(f)

# Step 3: Convert to DataFrame
df = pd.DataFrame(data)

# Step 4: Clean data

# Remove duplicates
df = df.drop_duplicates(subset=["post_id"])

# Remove rows with missing title
df = df.dropna(subset=["title"])

# Fill missing numeric values
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)

# Step 5: Save cleaned CSV
output_file = "data/trends_clean.csv"
df.to_csv(output_file, index=False)

print("Cleaned data saved to", output_file)
print("Total rows:", len(df))
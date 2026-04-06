import pandas as pd
import os

# Step 1: Load cleaned CSV
file_path = "data/trends_clean.csv"

if not os.path.exists(file_path):
    print("CSV file not found!")
    exit()

df = pd.read_csv(file_path)

print("\nTotal stories:", len(df))

# Step 2: Top 5 stories by score
top_stories = df.sort_values(by="score", ascending=False).head(5)

print("\nTop 5 Stories:")
print(top_stories[["title", "score"]])

# Step 3: Category counts
category_counts = df["category"].value_counts()

print("\nStories per Category:")
print(category_counts)

# Step 4: Average score per category
avg_score = df.groupby("category")["score"].mean()

print("\nAverage Score per Category:")
print(avg_score)

# Step 5: Most active authors
top_authors = df["author"].value_counts().head(5)

print("\nTop Authors:")
print(top_authors)
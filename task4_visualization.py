import pandas as pd
import matplotlib.pyplot as plt
import os

# Step 1: Load cleaned CSV
file_path = "data/trends_clean.csv"

if not os.path.exists(file_path):
    print("CSV file not found!")
    exit()

df = pd.read_csv(file_path)

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# -------------------------------
# Chart 1: Top 10 Stories
# -------------------------------
top10 = df.sort_values(by="score", ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# -------------------------------
# Chart 2: Category Distribution
# -------------------------------
category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))
category_counts.plot(kind="bar")
plt.title("Stories per Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("outputs/chart2_categories.png")
plt.close()

# -------------------------------
# Chart 3: Score vs Comments
# -------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df["score"], df["num_comments"])
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# -------------------------------
# Dashboard (All Charts Together)
# -------------------------------
plt.figure(figsize=(12, 8))

# Subplot 1
plt.subplot(2, 2, 1)
plt.barh(top10["title"], top10["score"])
plt.title("Top Stories")

# Subplot 2
plt.subplot(2, 2, 2)
category_counts.plot(kind="bar")
plt.title("Categories")

# Subplot 3
plt.subplot(2, 2, 3)
plt.scatter(df["score"], df["num_comments"])
plt.title("Score vs Comments")

# Subplot 4
plt.subplot(2, 2, 4)
df["num_comments"].hist()
plt.title("Comments Distribution")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in outputs folder!")

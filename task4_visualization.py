import pandas as pd
import matplotlib.pyplot as plt
import os

# Load CSV
file_path = "data/trends_clean.csv"

if not os.path.exists(file_path):
    print("CSV not found!")
    exit()

df = pd.read_csv(file_path)

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# -------------------------------
# Chart 1: Top 10 stories by score
# -------------------------------
top10 = df.sort_values(by="score", ascending=False).head(10)

plt.figure()
plt.barh(top10["title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# -------------------------------
# Chart 2: Category distribution
# -------------------------------
category_counts = df["category"].value_counts()

plt.figure()
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
plt.figure()
plt.scatter(df["score"], df["num_comments"])
plt.xlabel("Score")
plt.ylabel("Comments")
plt.title("Score vs Comments")
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# -------------------------------
# Chart 4: Dashboard (combined)
# -------------------------------
plt.figure(figsize=(10,8))

# Subplot 1
plt.subplot(2,2,1)
category_counts.plot(kind="bar")
plt.title("Categories")

# Subplot 2
plt.subplot(2,2,2)
plt.scatter(df["score"], df["num_comments"])
plt.title("Score vs Comments")

# Subplot 3
plt.subplot(2,2,3)
df["score"].hist()
plt.title("Score Distribution")

# Subplot 4
plt.subplot(2,2,4)
df["num_comments"].hist()
plt.title("Comments Distribution")

plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()

print("All charts saved in outputs folder!")
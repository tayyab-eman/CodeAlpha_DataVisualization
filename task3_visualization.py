import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# Load dataset
# -----------------------------
file_path = "data/country_population.csv"

df = pd.read_csv(file_path)

# Clean population column
df["population"] = (
    df["population"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace(" ", "", regex=False)
)

df["population"] = pd.to_numeric(
    df["population"],
    errors="coerce"
)

# Remove missing population values
df = df.dropna(subset=["population"])

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# -----------------------------
# Remove World aggregate
# -----------------------------
country_df = df[
    df["country"].str.lower() != "world"
].copy()

# -----------------------------
# 1. Top 10 Most Populated
# -----------------------------
top10 = country_df.nlargest(
    10,
    "population"
)

plt.figure(figsize=(12, 7))

plt.barh(
    top10["country"][::-1],
    top10["population"][::-1]
)

plt.title(
    "Top 10 Most Populated Locations"
)

plt.xlabel("Population")

plt.ylabel("Location")

plt.tight_layout()

plt.savefig(
    "outputs/top10_population_visualization.png",
    dpi=300
)

plt.show()

# -----------------------------
# 2. Population Share
# -----------------------------
top8 = country_df.nlargest(
    8,
    "population"
)

plt.figure(figsize=(9, 9))

plt.pie(
    top8["population"],
    labels=top8["country"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title(
    "Population Share of Top 8 Locations"
)

plt.tight_layout()

plt.savefig(
    "outputs/population_share_pie.png",
    dpi=300
)

plt.show()

# -----------------------------
# 3. Population Distribution
# -----------------------------
plt.figure(figsize=(10, 6))

plt.hist(
    country_df["population"],
    bins=30
)

plt.title(
    "Population Distribution Across Locations"
)

plt.xlabel("Population")

plt.ylabel("Number of Locations")

plt.tight_layout()

plt.savefig(
    "outputs/population_distribution_visualization.png",
    dpi=300
)

plt.show()

# -----------------------------
# Create visualization report
# -----------------------------
with open(
    "outputs/visualization_summary.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        "CodeAlpha Data Analytics Internship - Task 3\n"
        "Data Visualization\n\n"
    )

    f.write(
        "Dataset: country_population.csv\n\n"
    )

    f.write(
        "Visualizations Created:\n"
    )

    f.write(
        "1. Top 10 Most Populated Locations - Bar Chart\n"
    )

    f.write(
        "2. Population Share of Top 8 Locations - Pie Chart\n"
    )

    f.write(
        "3. Population Distribution Across Locations - Histogram\n\n"
    )

    f.write(
        "The World aggregate was excluded from country/location "
        "comparisons so that the charts focus on individual locations.\n\n"
    )

    f.write(
        "Key Observation:\n"
    )

    f.write(
        "Population values vary substantially across locations, "
        "with a small number of locations having much larger "
        "populations than most others.\n"
    )

print("\n========== TASK 3 COMPLETED ==========")
print("Three visualizations have been created.")
print("Results are saved in the outputs folder.")
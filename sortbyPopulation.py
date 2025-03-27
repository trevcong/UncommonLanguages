import pandas as pd

# Load data from your CSV file
input_file = 'languages_needing_translation_clean.csv'  # Replace with your actual file name if different
try:
    df = pd.read_csv(input_file, encoding='utf-8')
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# Define a custom sort order for Population Group (largest to smallest)
population_order = {
    '10M+': 6,
    '500K - 9.99M': 5,
    '100K - 499K': 4,
    '10K - 99.9K': 3,
    '5K - 9.9K': 2,
    '1000 - 4999': 1,
    '0': 0
}

# Add a temporary column for sorting
df['SortOrder'] = df['Population Group'].map(lambda x: population_order.get(x, -1))  # -1 for unknown values

# Sort by SortOrder (descending) and drop the temporary column
df = df.sort_values(by='SortOrder', ascending=False).drop('SortOrder', axis=1)

# Save to a new CSV file
output_file = 'languages_sorted_by_population.csv'
df.to_csv(output_file, index=False)

print(f"Data saved to '{output_file}' sorted by Population Group (largest to smallest).")
print("Preview of sorted data (first few rows):")
print(df.head().to_string(index=False))

def main():
    print(">>> Saving languages sorted by Population Group")
    print(df.to_string(index=False))

if __name__ == "__main__":
    main()
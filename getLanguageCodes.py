
import pandas as pd

# Load your CSV
input_file = 'languages_sorted_by_population.csv'
try:
    df = pd.read_csv(input_file, encoding='utf-8')
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# Optional: Filter for 10M+ languages (comment out if you want all 4,909)
# df = df[df['Population Group'] == '10M+']

# Get unique language codes, converting to string and dropping NaN
language_codes = df['Language Code'].dropna().astype(str).unique()
print(f"Found {len(language_codes)} unique language codes.")

# Save to a text file
with open('language_codes.txt', 'w') as f:
    f.write('\n'.join(language_codes))

print("Language codes saved to 'language_codes.txt'")
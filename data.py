import pandas as pd

# Try loading the CSV with different encodings and delimiter options
try:
    # Attempt UTF-8 with BOM first
    df = pd.read_csv('Details.csv', encoding='utf-8-sig')
except UnicodeDecodeError:
    # Fallback to UTF-16, likely tab-separated based on error
    try:
        df = pd.read_csv('Details.csv', encoding='utf-16', sep='\t')
    except pd.errors.ParserError as e:
        print(f"ParserError with UTF-16 and tab delimiter: {e}")
        # Try skipping bad lines as a last resort
        df = pd.read_csv('Details.csv', encoding='utf-16', sep='\t', on_bad_lines='skip')
except Exception as e:
    print(f"Error loading file: {e}")
    exit()

# Clean the data
# Extract language code from Language Name, if present
df['Language Code'] = df['Language Name'].str.extract(r'\[(.*?)\]')
df['Language Name'] = df['Language Name'].str.replace(r'\s*\[.*?\]', '', regex=True)
# Replace empty strings with NaN
df.replace('', pd.NA, inplace=True)
# Standardize Scripture values
df['Scripture'] = df['Scripture'].fillna('Not Shown')

# Filter languages needing translation
needs_translation = df[
    (df['Scripture'] != 'Bible') &
    (df['Active Translation'] != 'Yes') &
    (df['Population Group'] != '0')
]

# Sort by Population Group and Language Name
needs_translation = needs_translation.sort_values(by=['Population Group', 'Language Name'], ascending=[False, True])

# Display results
print("Languages Needing Biblical Translation:")
print(needs_translation[['Country', 'Language Name', 'Language Code', 'Population Group', 'Language Vitality', 'Scripture']])

# Save to CSV
needs_translation.to_csv('languages_needing_translation.csv', index=False)
print("\nResults saved to 'languages_needing_translation.csv'")

def main():
    print(">>> Cleaning and filtering languages needing translation from Details.csv")
    print(needs_translation[['Country', 'Language Name', 'Language Code', 'Population Group', 'Language Vitality', 'Scripture']])

if __name__ == "__main__":
    main()
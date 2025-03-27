# Read the existing language codes
input_file = 'language_codes.txt'
with open(input_file, 'r') as f:
    codes = f.read().splitlines()

# Remove duplicates (case-insensitive) and filter out empty lines
unique_codes = sorted(set(code.lower() for code in codes if code.strip()), key=str.lower)
print(f"Original count: {len(codes)}")
print(f"Unique count after removing duplicates: {len(unique_codes)}")

# Save the cleaned list
output_file = 'unique_language_codes.txt'
with open(output_file, 'w') as f:
    f.write('\n'.join(unique_codes))

print(f"Unique language codes saved to '{output_file}'")
import csv

# List of countries with <2% Christianity
low_christianity_countries = {
    "Afghanistan", "Algeria", "Bangladesh", "Bhutan", "Iran", "Maldives", 
    "Mauritania", "Morocco", "Niger", "North Korea", "Pakistan", "Saudi Arabia", 
    "Somalia", "Sudan", "Tunisia", "Turkey", "Yemen"
}

# Input and output file names
input_file = "languages_sorted_by_population.csv"
output_file = "filtered_low_christianity_countries.csv"

def filter_data():
    # Open the input CSV and read it
    with open(input_file, newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        # Ensure all expected columns are present
        headers = reader.fieldnames
        
        # Open the output CSV and write the filtered data
        with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=headers)
            writer.writeheader()
            
            # Filter rows where the country is in the low Christianity list
            for row in reader:
                if row["Country"] in low_christianity_countries:
                    writer.writerow(row)

def main():
    print(f"Filtering data from {input_file}...")
    filter_data()
    print(f"Filtered data saved to {output_file}")

if __name__ == "__main__":
    main()
import csv

def tsv_to_csv(tsv_file, csv_file):
    # Open the TSV file for reading
    with open(tsv_file, 'r', newline='') as tsv_f:
        # Open the CSV file for writing
        with open(csv_file, 'w', newline='') as csv_f:
            # Create a csv reader object using a tab delimiter
            tsv_reader = csv.reader(tsv_f, delimiter='\t')
            # Create a csv writer object
            csv_writer = csv.writer(csv_f)
            
            # Write all rows from the TSV file to the CSV file
            for row in tsv_reader:
                csv_writer.writerow(row)

# Example usage
tsv_file_path = 'input_file.tsv'  # Replace with your TSV file path
csv_file_path = 'output_file.csv'  # Replace with your desired CSV file path

tsv_to_csv(tsv_file_path, csv_file_path)

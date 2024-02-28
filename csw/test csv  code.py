import csv

def open_csv_file(105657.):
    try:
        with open(105657., 'r', newline='') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)  # You can process each row as needed
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Example usage:
filename = '105657.csv'  # Replace 'example.csv' with the path to your CSV file
open_csv_file(filename)

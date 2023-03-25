import csv

def read_csv_to_set(file_path, delimiter):
    # Create an empty set to store the data
    data_set = set()

    # Open the file and read the data into the set
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        for row in reader:
            data_set.add(row[0])

    # Return the set
    return data_set

# Print the hashtable
full_strength_set = read_csv_to_set('full_strength.txt', '\t')
attendees_set = read_csv_to_set('attendees.txt', '\t')

print("Full strength size:",len(full_strength_set))
print("Attendees size    :",len(attendees_set))
print("Absentees         :",full_strength_set-attendees_set)

with open('Results.txt', 'w') as f:
    f.write(f"Full strength size: {len(full_strength_set)}\n")
    f.write(f"Attendees size    : {len(attendees_set)}\n")
    f.write(f"Absentees         : {full_strength_set-attendees_set}\n")
""" CSV file read write """
import csv

#  reading from csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        print('\n')
        print(row[0], row[1], row[2])


# csv file writing
with open("csv_write.csv", 'w', newline='') as file:
    write = csv.writer(file)
    write.writerow(["SN", "Movie", "Protagonist"])
    write.writerow([1, "Lord of the Ring", "Frodo Baggins"])
    write.writerow([2, "Harry Potter", "Harry Potter"])
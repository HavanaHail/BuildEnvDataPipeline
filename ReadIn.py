##Read in data
import csv


def read_in(csv_name):
    with open(csv_name,mode = 'r')as file:
        csvFile = csv.reader(file)

        for lines in csvFile:
            print(lines)

import csv
# starting struct




rows = []
with open("O2Ring_20221118173026_OXIRecord.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

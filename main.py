import csv
# starting struct
j = "hailey"
class User(object):
    pass
name = j + "user"
print(name)
a = User()
a.csvhead = []
a.csvrows = []


rows = []
with open("O2Ring_20221118173026_OXIRecord.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
#print(header)
#print(rows)
a.csvhead = header
a.csvrows = rows
print(a.csvhead)
print(a.csvrows)
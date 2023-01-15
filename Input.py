import csv

from numpy import double


class Result:
    id = 0

filePath = "CSV/test/Built_Environment_Survey_January 15_2023_12_24.csv"


f = open(filePath, 'r')
reader = csv.reader(f)

results = {}

for row in reader:
    results[row[0]] = {'PANAS_PA':(double(row[1]))/10, 'PANAS_NA':(double(row[2]))/10, 'PANAS_SN':(double(row[3]))/3}

print(results)
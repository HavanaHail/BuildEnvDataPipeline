import pymongo
from pymongo import MongoClient
import csv
import json
import pandas as pd
import numpy as np



# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            # Assuming a column named 'No' to
            # be the primary key
            key = rows["RecordedDate"]
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))


# Driver Code

# Decide the two file paths according to your
# computer system
#csvFilePath = r'Names.csv'
#jsonFilePath = r'Names.json'

# Call the make_json function
#make_json(csvFilePath, jsonFilePath)

make_json("CSV/test/Built Environment Survey_January 30, 2023_20.24-2.csv", "CSV/test/Built Environment Survey_January 30, 2023_20.24-2.json")

client = MongoClient("mongodb://localhost:27017/");

db = client["BENV"]

Collection = db["PANAS"]

with open("CSV/test/Built Environment Survey_January 30, 2023_20.24-2.json") as file:
    file_data = json.load(file)
 # Inserting the loaded data in the Collection
 # if JSON contains data more than one entry
 # insert_many is used else insert_one is used
if isinstance(file_data, list):
    Collection.insert_many(file_data)
else:
    Collection.insert_one(file_data)

def o2ToCSV(heartBeat, time, target):
    arr = np.asarray([heartBeat, time])
    data = pd.DataFrame(arr).to_csv(target, header =['HeartBeat', 'Time'])
    return data





import csv
import sys,os

import numpy as np
import pandas as pd

from numpy import double


class Experiment:
    def __init__(self, idNum, o2csv, eeg, panas1, panas2, info):
        self.idNum = idNum
        self.o2csv = o2csv
        self.eeg = eeg
        self.panas1 = panas1
        self.panas2 = panas2
        self.info = info

def createExperiment():
    #idNum = sys.argv[1]
    #folder_path = sys.argv[2]

    idNum = 1856
    folder_path = '/Users/nwhalen/Developer/MQP/BuildEnvDataPipeline/EMILY'
    #target_path = '/Users/nwhalen/Developer/MQP/BuildEnvDataPipeline/EMILY'
    panasCount = 0
    target_path = os.path.join(folder_path, "Result" + str(idNum))
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for file in os.listdir(folder_path):
        f = os.path.join(folder_path, file)
        if os.path.isfile(f): ##CHECKS IN RESULT FOLDER - NOT GOOD
            #print(os.path.basename(f))
            if  'O2' in os.path.basename(f):
                #Process o2 data Todo

                print(os.path.basename(f))
            elif 'EEG' in os.path.basename(f):
                    #Process eeg data Todo
                print(os.path.basename(f))
            elif 'PANAS' in os.path.basename(f):
                    #Process panas data Todo
                if(panasCount < 2):
                    data = getPanasScores("/Users/nwhalen/Developer/MQP/BuildEnvDataPipeline/CSV/test/CSVTEST_PANAS.csv", 1856)
                    panasCount = panasCount + 1
                    target = target_path + '/' + 'PANAS' + str(panasCount) +'.csv' ##Panas number hardcoded for now
                    pd.DataFrame(data).to_csv(target, index_label="i", header=['Time/Date','PANAS_PA','PANAS_NA','PANAS_SN','ID'])




def getPanasScores(target, idNum):
    csv_file = csv.reader(open(target, "r"), delimiter=",")
    panasCount = 1
    array = []

    for row in csv_file:
        strId = str(idNum)
        # if current rows 2nd value is equal to input, print that row
        if strId == row[4]:
            #print(row)
            array.append(row)
    #print(array)
    result = np.asarray(array)
    return result

# def readPANAS(filePath):
#     #filePath = input("Enter CSV filepath:\n")
#     f = open(filePath, 'r')
#     reader = csv.reader(f)
#     results = {}
#
#     for row in reader:
#         results[row[0]] = {'PANAS_PA': (double(row[1])) / 10, 'PANAS_NA': (double(row[2])) / 10,
#                            'PANAS_SN': (double(row[3])) / 3}
#
#     #print(f"results: {results}")
#     return results
# def readPANAS2(filePath):
#     with open(filePath, 'r') as data:
#         for line in csv.reader(data):
#             print(line)
#         return data

# def panasToCSV(target, dict):
#     field_names = ['PANAS_PA', 'PANAS_NA', 'PANAS_SN']
#
#     with open(target, 'w') as csvFile:
#         print(target)
#         writer = csv.DictWriter(csvFile, fieldnames=field_names)
#         writer.writeheader()
#        # print(dict)
#         writer.writerows(dict) ##NOT WORKING - I/O operation on closed file
#         return csvFile


if __name__ == '__main__':
    createExperiment()
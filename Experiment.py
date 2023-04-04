import csv
import sys,os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import nan
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
    #folder_path = sys.argv[2] --> Where the folder is located

    #ASk questions about - Who ran the experiment & Start and end time & brief report and put into text file

    idNum = 1856 #hardcoded for now
    folder_path = '/Users/nwhalen/Developer/MQP/BuildEnvDataPipeline/EMILY'
    #target_path = '/Users/nwhalen/Developer/MQP/BuildEnvDataPipeline/EMILY'
    panasCount = 0
    target_path = os.path.join(folder_path, "Result" + str(idNum))
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for file in os.listdir(folder_path):
        f = os.path.join(folder_path, file)
        if os.path.isfile(f):
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
                    data = getPanasScores("/Users/nwhalen/Developer/MQP/BuildEnvDataPipeline/CSV/test/CSVTEST_PANAS.csv", idNum)
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

#Reading in O2
rows = []
heartRate = []
clock = []
def readInO2ring():
    
    ave = []
    with open("O2Ring_20230213132922.csv", 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)
    print(header)
    
    # Way to specify which column we are using
    mean = 0
    count = 0
    watch = 0
    lastbmp = 0
    # Check for motion
    time = 0
    sp02 =1
    pulse =2 
    motion =3 
    sp02reminder =4
    pulseReminder = 5
    for i in range(len(rows)):
        # Turn each row into a list of each thing in row
    # print (time, sp02, pulse, motion, sp02reminder, pulseReminder)
        if int(rows[i][pulse]) > 60 and int(rows[i][pulse]) < 100:
            # if int(pulse)<= lastbmp+7 and int(pulse)>=lastbmp-7 or lastbmp == 0:
           # print(watch, pulse)
            mean += int(rows[i][pulse])
            count += 1
            heartRate.append(int(rows[i][pulse]))
            clock.append(watch)
            rows[i][time] = watch
            # else:
            #   heartRate.append(np.nan)
            #  clock.append(watch)
        else:
            heartRate.append(np.nan)
            rows[i][pulse] = np.nan
            clock.append(watch)
            rows[i][time] = watch
        watch += 4
       # lastbmp = int(pulse)
        
    #  paresedRow = row.split(",")
        # print(row)
    ave = int(mean/count)
    
def writeO2Data():
    with open('cleanedO2Ring.csv', 'w') as cleaned:
        fieldnames = ['time','O2','heart rate','motion','02reminder','pulsereminder']
        writer = csv.DictWriter(cleaned, fieldnames = fieldnames)
        writer.writeheader()
        writer = csv.writer(cleaned, delimiter=',')
        for row in rows:
            writer.writerow(row)



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
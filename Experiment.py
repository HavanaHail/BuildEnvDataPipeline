import csv
import sys,os

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

    idNum = 1
    folder_path = '/Users/nwhalen/Developer/MQP/BuildEnvDataPipeline/EMILY'
    #target_path = '/Users/nwhalen/Developer/MQP/BuildEnvDataPipeline/EMILY'
    panasCount = 1
    target_path = os.path.join(folder_path, "Result")
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    for file in os.listdir(folder_path):
        f = os.path.join(folder_path, file)
        if  os.path.isfile(f):
            #print(os.path.basename(f))
            if  'O2' in os.path.basename(f):
                #Process o2 data Todo

                print(os.path.basename(f))
            elif 'EEG' in os.path.basename(f):
                    #Process eeg data Todo
                print(os.path.basename(f))
            elif 'PANAS' in os.path.basename(f):
                    #Process panas data Todo
                PANAS_DAT = readPANAS(f)
                print(PANAS_DAT)
                    ##ADD TO FOLDER
                target = target_path + '/' + 'PANAS' + '1'
                print(target)
                PANAS_RES = panasToCSV(target, PANAS_DAT)

                panasCount = panasCount + 1
                print(os.path.basename(f))



def readPANAS(filePath):
    #filePath = input("Enter CSV filepath:\n")
    f = open(filePath, 'r')
    reader = csv.reader(f)
    results = {}

    for row in reader:
        results[row[0]] = {'PANAS_PA': (double(row[1])) / 10, 'PANAS_NA': (double(row[2])) / 10,
                           'PANAS_SN': (double(row[3])) / 3}

    #print(f"results: {results}")
    return results

def panasToCSV(target, dict):
    field_names = ['PANAS_PA', 'PANAS_NA', 'PANAS_SN']
    with open(target, 'w') as csvFile:
        print(target)
        writer = csv.DictWriter(csvFile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(dict) ##NOT WORKING

if __name__ == '__main__':
    createExperiment()
import csv
import struct

# starting struct
participantsCount = 0 

class Participant:
    def __init__(self,idNum, o2Csv,eegEdf,eegCsv,video,qualtrics):
    self.idNum = idNum;
    self.o2Csv = o2Csv;
    self.eegEdf = eegEdf;
    self.eegCsv = eegCsv;
    self.video = video;
    self.qualtrics = qualtrics;
    participantsCount+=1


rows = []
with open("O2Ring_20221118173026_OXIRecord.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
print(rows)

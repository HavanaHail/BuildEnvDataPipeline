import csv
import struct

# starting struct
participantsCount = 0 

class Participant:
    def __init__(self,idNum, o2Csv,eegEdf,eegCsv,video,panas1, panas2, date, recorder, room, universalTime):
        self.idNum = idNum;
        self.o2Csv = o2Csv;
        self.eegEdf = eegEdf;
        self.eegCsv = eegCsv;
        self.video = video;
        self.panas1 = panas1;
        self.panas2 = panas2;
        self. date = date;
        self.recorder = recorder;
        self.room = room;
        self.univeralTime = universalTime;
        participantsCount+=1


rows = []
with open("sebastian 11-18\O2Ring_20221118173026_OXIRecord.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
for row in rows:  
    #Turn each row into a list of each thing in row 

    print(row)

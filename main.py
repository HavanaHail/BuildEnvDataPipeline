import csv
import struct
import matplotlib.pyplot as plt

import typer

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
heartRate = []
clock = []
ave = []
with open("O2Ring_20221118173026_OXIRecord.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
#Way to specify which column we are using
mean = 0
count = 0

for time, sp02, pulse, motion, sp02reminder, pulseReminder in rows:  
    #Turn each row into a list of each thing in row 
    print (time, sp02, pulse, motion, sp02reminder, pulseReminder)
    if int(pulse)>50 and int(pulse)<150:
        mean += int(pulse)
        count +=1
        heartRate.append(int(pulse))
        clock.append(time[0:7])
  #  paresedRow = row.split(",")
    #print(row)
ave = int(mean/count)
print("Pulse average is: ", ave)
plt.plot(clock,heartRate, label = 'Pulse')
plt.axhline(y=ave, color = 'r', linestyle = 'dashed', label = 'Average')
plt.xlabel('time')
plt.ylabel('heartrate')
plt.xticks(rotation=90,fontsize='small')
plt.title('participant #')
plt.show()

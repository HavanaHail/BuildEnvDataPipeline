import csv
import struct
import matplotlib.pyplot as plt
import numpy as np
from numpy import nan

import typer

# starting struct
participantsCount = 0

class Participant:
    def __init__(self,idNum, o2Csv,eegEdf,eegCsv,video,panas1, panas2, date, recorder, room, universalTime):
        self.idNum = idNum
        self.o2Csv = o2Csv
        self.eegEdf = eegEdf
        self.eegCsv = eegCsv
        self.video = video
        self.panas1 = panas1
        self.panas2 = panas2
        self. date = date
        self.recorder = recorder
        self.room = room
        self.univeralTime = universalTime
        #participantsCount+=1


rows = []
heartRate = []
clock = []
ave = []
with open("O2Ring_20230213132922.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
print(header)
#Way to specify which column we are using
mean = 0
count = 0
watch = 0
lastbmp = 0
#Check for motion
for time, sp02, pulse, motion, sp02reminder, pulseReminder in rows:  
    #Turn each row into a list of each thing in row 
   # print (time, sp02, pulse, motion, sp02reminder, pulseReminder)
    if int(pulse)>60 and int(pulse)<100:
        #if int(pulse)<= lastbmp+7 and int(pulse)>=lastbmp-7 or lastbmp == 0:
            print(watch, pulse)
            mean += int(pulse)
            count +=1
            heartRate.append(int(pulse))
            clock.append(watch)
        #else:
         #   heartRate.append(np.nan)
          #  clock.append(watch)
    else:
        heartRate.append(np.nan)
        clock.append(watch)
    watch +=4
    lastbmp = int(pulse)
  #  paresedRow = row.split(",")
    #print(row)
ave = int(mean/count)
#writing in new cleaned data
#fields = ['time','heartrate']
#name = "CleanedData" + ".csv"
#with open(name,'w') as csvfile:
#    for pulse in heartRate:
        
#Put NA when the number bad don't cut it 
print("Pulse average is: ", ave)
plt.plot(clock,heartRate, label = 'Pulse')
plt.axhline(y=ave, color = 'r', linestyle = 'dashed', label = 'Average')
#plt.axvline(x=120,color ='g',linestyle ='dashed')
#plt.axvline(x=300,color ='g',linestyle ='dashed')
# plt.axvline(x=800,color ='g',linestyle ='dashed')
plt.xlabel('time (secs)')
plt.ylabel('heartrate')
plt.xticks(rotation=90,fontsize='small')
plt.title('participant #')
plt.show()
import csv
import struct
import matplotlib.pyplot as plt
import numpy as np
import sys, os
from numpy import nan

rows = []
heartRate = []
clock = []
def readInO2ring():
    
    ave = []
    with open("sebastian 11-18/O2Ring_20230213132922.csv", 'r') as file:
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

                

if __name__ == '__main__':
    readInO2ring()
    writeO2Data()







#writing in new cleaned data
#fields = ['time','heartrate']
#name = "CleanedData" + ".csv"
#with open(name,'w') as csvfile:
#    for pulse in heartRate:

#Put NA when the number bad don't cut it
#print("Pulse average is: ", ave)
#plt.plot(clock,heartRate, label = 'Pulse')
#plt.axhline(y=ave, color = 'r', linestyle = 'dashed', label = 'Average')
#plt.axvline(x=120,color ='g',linestyle ='dashed')
#plt.axvline(x=300,color ='g',linestyle ='dashed')
# plt.axvline(x=800,color ='g',linestyle ='dashed')
#plt.xlabel('time (secs)')
#plt.ylabel('heartrate')
#plt.xticks(rotation=90,fontsize='small')
#plt.title('participant #')
#plt.show()

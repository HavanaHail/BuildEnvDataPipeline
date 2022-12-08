import numpy as np
import mne
#raw = mne.io.read_raw_edf("opensignals_scrappy.edf", None, None,'auto', (), False, None)
#importing library
import matplotlib.pyplot as plt
import csv
#datasets



#edf = mne.io.read_raw_edf('opensignals_scrappy.edf')
#header = ','.join(edf.ch_names)
#np.savetxt('pls.csv', edf.get_data().T, delimiter=',', header=header)

# opening the CSV file
with open('pls.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  yvalues = []
  xvalues = []
  y = 0
  x =  1
  for lines in csvFile:
        yvalues.append(y)
        y = y + 1

        #print(type(lines))
        x = int(format(float(lines[0]), 'f'))
        xvalues.append(x)
        x = x+1
       # print(lines[0])
        #print(lines)
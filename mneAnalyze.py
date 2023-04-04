#import biosignalsnotebooks as bsnb
#import numpy as np
#import pandas as pd

from h5py import File

# Package intended to work with arrays
from numpy import array

# biosignalsnotebooks python package
import biosignalsnotebooks as bsnb
file_folder = ""
file_path ="EMILY\emily0007804b1875_2022-12-15_16-24-08-tfr.h5"

h5_object = File(file_path)

# Keys list (.h5 hierarchy ground level)
list(h5_object.keys())


h5_group = h5_object.get('00:07:80:3B:46:61')
print ("Second hierarchy level: " + str(list(h5_group)))

print ("Metadata of h5_group: \n" + str(list(h5_group.attrs.keys())))

sampling_rate = h5_group.attrs.get("sampling rate")
print ("Sampling Rate: " + str(sampling_rate))

h5_sub_group = h5_group.get("raw")
print("Third hierarchy level: " + str(list(h5_sub_group)))

h5_data = h5_sub_group.get("channel_1")

# Conversion of a nested list to a flatten list by list-comprehension
# The following line is equivalent to:
# for sublist in h5_data:
#    for item in sublist:
#        flat_list.append(item)
data_list = [item for sublist in h5_data for item in sublist]
time = bsnb.generate_time(data_list, sampling_rate)

# Signal data samples values and graphical representation.
print (array([item for sublist in h5_data for item in sublist]))
bsnb.plot([time], [data_list], x_axis_label="Time (s)", y_axis_label="Raw Data")


##################################################################################################################

import biosignalsnotebooks as bsnb
import numpy as np
import pandas as pd

file_path = "demo.h5"

# Loading Data
data, header = bsnb.load(file_path)
print ("\033[1mHeader:\n\033[0m" + str(header) + "\n\033[1mData:\033[0m\n" + str(data))

channel_data = [data['CH1'], data['CH2'], data['CH3']]


# to np array
np_data = np.array(channel_data)
print(np_data.shape())
print(np_data[0])


# to pd DataFrame
pd_df = pd.DataFrame(data=channel_data, columns=["CH1", "CH2", "CH3"])
display(pd_df.head(10))
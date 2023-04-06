#import biosignalsnotebooks as bsnb
#import numpy as np
#import pandas as pd
import biosignalsnotebooks as bsnb
import h5py
from jinja2.utils import markupsafe
from markupsafe import Markup

# Package intended to work with arrays
from numpy import array

markupsafe.Markup()
Markup('')

file_folder = ""
file_path ="/Users/nwhalen/Developer/MQP/BuildEnvDataPipeline/EMILY/emily0007804b1875_2022-12-15_16-24-08_tfr.h5"

h5_object = h5py.File(file_path)
a_group_key = list(h5_object.keys())[0]

# get the object type for a_group_key: usually group or dataset
print(type(h5_object[a_group_key]))

print("Keys: %s" % h5_object.keys())


# Keys list (.h5 hierarchy ground level)
list(h5_object.keys())


#h5_group = h5_object.get('00:07:80:3B:46:61')
#h5_group = h5_object.get('00:07:80:4B:18:75')
h5_group = h5_object.get(a_group_key)
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

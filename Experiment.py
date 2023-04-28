import csv
import sys, os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import h5py
from bokeh.plotting import figure
from jinja2.utils import markupsafe
from markupsafe import Markup
from bokeh.io import output_file, show
from numpy import nan, average
from numpy import random
import biosignalsnotebooks as bsnb


##Object unused in final implementation
class Experiment:
    def __init__(self, idNum, o2csv, eeg, panas1, panas2, info):
        self.idNum = idNum
        self.o2csv = o2csv
        self.eeg = eeg
        self.panas1 = panas1
        self.panas2 = panas2
        self.info = info


##Main function
def createExperiment():
    idNum = sys.argv[1]
    folder_path = sys.argv[2]  # --> Where the folder is located

    # Ask questions about - Who ran the experiment & Start and end time & brief report and put into text file
    panasCount = 0

    target_path = os.path.join(folder_path, "Result" + str(idNum))

    if not os.path.exists(target_path):
        os.mkdir(target_path)
    textFilePath = target_path + "/report.txt"
    writeReport(textFilePath)
    for file in os.listdir(folder_path):
        f = os.path.join(folder_path, file)
        if os.path.isfile(f):
            if 'O2' in os.path.basename(f):
                # Process o2 data
                readInO2ring(f, target_path)
            elif 'h5' in os.path.basename(f):
                # Process eeg data
                readEeg(f, target_path)
            elif 'PANAS' in os.path.basename(f):
                # Process panas data
                if (panasCount < 2):
                    data = getPanasScores(f, idNum)
                    panasCount = panasCount + 1
                    target = target_path + '/' + 'PANAS' + str(panasCount) + '.csv'
                    pd.DataFrame(data).to_csv(target, index_label="i",
                                              header=['Time/Date', 'PANAS_PA', 'PANAS_NA', 'PANAS_SN', 'ID'])

## Pull scores matching idNum from PANAS csv
def getPanasScores(target, idNum):
    csv_file = csv.reader(open(target, "r"), delimiter=",")
    array = []

    for row in csv_file:
        strId = str(idNum)
        # if current rows 2nd value is equal to input, print that row
        if strId == row[4]:
            array.append(row)
    result = np.asarray(array)
    return result


# Reading in O2
rows = []
heartRate = []
clock = []

##O2 Ring csv
def readInO2ring(fileName, targetPath):
    ave = []
    with open(fileName, 'r') as file:
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            rows.append(row)

    # Way to specify which column we are using
    mean = 0
    count = 0
    watch = 0
    lastbmp = 0
    # Check for motion
    time = 0
    sp02 = 1
    pulse = 2
    motion = 3
    sp02reminder = 4
    pulseReminder = 5
    for i in range(len(rows)):
        # Turn each row into a list of each thing in row
        if int(rows[i][pulse]) > 60 and int(rows[i][pulse]) < 100:
            mean += int(rows[i][pulse])
            count += 1
            heartRate.append(int(rows[i][pulse]))
            clock.append(watch)
            rows[i][time] = watch
        else:
            heartRate.append(np.nan)
            rows[i][pulse] = np.nan
            clock.append(watch)
            rows[i][time] = watch
        watch += 4
    ave = int(mean / count)
    makeGraph(heartRate, clock, ave)
    writeO2Data(fileName, targetPath)

##O2 data into csv
def writeO2Data(fileName, targetPath):
    with open(targetPath + "/02.csv", 'w') as cleaned:
        fieldnames = ['time', 'O2', 'heart rate', 'motion', '02reminder', 'pulsereminder']
        writer = csv.DictWriter(cleaned, fieldnames=fieldnames)
        writer.writeheader()
        writer = csv.writer(cleaned, delimiter=',')
        for row in rows:
            writer.writerow(row)


##Data visualization
def makeGraph(pulse, time, mean):

    plt.plot(time, pulse, label='Pulse Over Time')
    plt.axhline(y=mean, color='r', linestyle='dashed', label='Average')
    plt.xlabel('time(secs)')
    plt.ylabel('heartrate')
    plt.show()

##Text file with report of experiment.
def writeReport(filePath):
    names = input("Please enter the names of the people who ran the experiment.\n")
    summary = input("Please provide a brief summary of the experiment\n")
    data = [names, summary]
    with open(filePath, "w") as txt_file:
        for line in data:
            txt_file.write("".join(line) + "\n")


##Read h5 eeg file
def readEeg(filePath, targetPath):
    markupsafe.Markup()
    Markup('')

    output_file(targetPath + "/eegVis.html")

    file_folder = ""

    h5_object = h5py.File(filePath)
    a_group_key = list(h5_object.keys())[0]


    # get the object type for a_group_key: usually group or dataset
    print(type(h5_object[a_group_key]))

    print("Keys: %s" % h5_object.keys())

    # Keys list (.h5 hierarchy ground level)
    list(h5_object.keys())

    h5_group = h5_object.get(a_group_key)
    print("Second hierarchy level: " + str(list(h5_group)))

    print("Metadata of h5_group: \n" + str(list(h5_group.attrs.keys())))

    sampling_rate = h5_group.attrs.get("sampling rate")
    print("Sampling Rate: " + str(sampling_rate))

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
    # print (array([item for sublist in h5_data for item in sublist]))
    # bsnb.plot([time], [data_list], x_axis_label="Time (s)", y_axis_label="Raw Data", show_plot=False, save_plot=True)

    data = np.array([time, data_list]).transpose()
    df = pd.DataFrame(data)
    df.to_csv(targetPath + "/eeg.csv", header=["Time", "Data"], index_label="i")

    # http://notebooks.pluxbiosignals.com/notebooks/Categories/Visualise/plot_acquired_data_single_rev.html

    data, header = bsnb.load(filePath, get_header=True)
    print("\033[1mHeader:\n\033[0m" + str(header) + "\n\033[1mData:\033[0m\n" + str(data))
    signal = data["CH1"]
    time = bsnb.generate_time(signal, header["sampling rate"])
    baseline = average(signal)
    baseline_shift = 0.50 * baseline
    data_noise = signal + random.normal(0, 1000, len(signal)) + baseline_shift
    bokeh_figure = figure(x_axis_label='Time (s)', y_axis_label='Raw Data')
    bokeh_figure.line(time, signal, legend_label="Original Data")
    bokeh_figure.line(time, data_noise, legend_label="Noisy Data")
    # show(bokeh_figure)
    bsnb.plot([time, time], [signal, data_noise], legend_label=["Original Data", "Noisy Data"],
              y_axis_label=["Raw Data", "Raw Data"], x_axis_label="Time (s)")


if __name__ == '__main__':
    createExperiment()

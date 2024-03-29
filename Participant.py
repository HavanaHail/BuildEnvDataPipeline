import csv
import sys
import pandas as pd
import typer
from numpy import double


class Experiment:
    def __init__(self, firstPanas, secondPanas, o2, eeg):
        self.firstPanas = firstPanas
        self.secondPanas = secondPanas
        self.o2 = o2
        self.eeg = eeg


class Participant:
    def __int__(self, id, first, second):
        self.id = id
        self.first = first
        self.second = second
app = typer.Typer()



@app.command()
def readPANAS(filePath):
    #filePath = input("Enter CSV filepath:\n")
    f = open(filePath, 'r')
    reader = csv.reader(f)
    results = {}

    for row in reader:
        results[row[0]] = {'PANAS_PA': (double(row[1])) / 10, 'PANAS_NA': (double(row[2])) / 10,
                           'PANAS_SN': (double(row[3])) / 3}

    print(f"results: {results}")
    return results


@app.command()
def readEEG(filePath):
    #filePath = input("Enter H5 filepath:\n")
    # f = open(filePath, 'r')
    results = {}
    # fpath = sys.argv[1]
    # if len(sys.argv) > 2:
    # key = sys.argv[2]
    # df = pd.read_hdf(fpath, key=key)
    # else:
    df = pd.read_hdf(filePath)
    df.to_csv(results, index=False)
    print(f"results: {results}")

#Pass in 4 filepaths
@app.command()
def createExperiment():
    Panas1 = readPANAS(sys.argv[2])
    Panas2 = readPANAS(sys.argv[3])
    o2 = sys.argv[4]
    eeg = sys.argv[5]
    e = Experiment(Panas1, Panas2, o2, eeg)
    print(e)
    return e

if __name__ == "__main__":
    createExperiment()
    app()

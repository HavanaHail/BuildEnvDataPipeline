import csv
import typer
from numpy import double

app = typer.Typer()


#filePath = "CSV/test/Built_Environment_Survey_January 15_2023_12_24.csv"
@app.command()
def readcsv():
    filePath = input("Enter CSV filepath:\n")
    f = open(filePath, 'r')
    reader = csv.reader(f)
    results = {}

    for row in reader:
        results[row[0]] = {'PANAS_PA':(double(row[1]))/10, 'PANAS_NA':(double(row[2]))/10, 'PANAS_SN':(double(row[3]))/3}

    print(f"results: {results}")

    #Add to database

if __name__ == "__main__":
    app()

import matplotlib.pyplot as plt
import csv
import os

if os.path.exists("data"):
    dir = os.listdir("data")
    for i in dir:
        if i.contains(".csv"):
            data = []
            with open(i,newline='') as csvfile:
                csvread = csv.reader(csvfile,delimiter=',')
                for row in csvread:
                    data.append(row[2:])
            print(data)
            plt.plot(data)
            plt.savefig(i.replace('csv','png'))
else:
    print("No directory 'data'!")
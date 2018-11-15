# import dependencies
import csv
import numpy as np


data = []
x = []
y = []

with open("Data/train.csv") as training_data:
    csv_file = csv.reader(training_data, delimiter=',')
    for row in csv_file:
        data.append(row)

print(len(data[0][1:len(data[0])]))

for i in range(1, len(data)):
    x.append(np.array(data[i][1:len(data[0])]))
    y.append(np.array(data[i][0]))

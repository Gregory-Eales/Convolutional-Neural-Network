# import dependencies
import csv
import numpy as np

def get_data():

	data = []
	x = []
	y = []

	with open("Data/train.csv") as training_data:
		csv_file = csv.reader(training_data, delimiter=',')
		for row in csv_file:
			data.append(row)
		for i in range(1, len(data)):
			x.append(np.reshape(np.array(data[i][1:len(data[0])]), [28, 28]))
			y.append(np.array(data[i][0]))
		x = np.array(x)
		y = np.array(y)
		return x, y
import numpy as np
import os
from tqdm import tqdm
import time


class Convolutional_Neural_Network(object):

	def __init__(self, x, y):
		
		# initiate parameters
		self.x = x
		self.y = y
		self.initial_shape = self.x.shape

		# convolutional weights
		self.conv_w = {}
		# fully connected weights
		self.ff_w = {}

	def pad(self, vector):
		return np.pad(vector, (1, 1), mode="constant")
		
	def convolve_window(self, v, w, step):
		w_length, w_width, w_height = w.shape[0], w.shape[1], w.shape(2)
		v_length, v_width, v_height = v.shape[0], v.shape[1], v.shape(2)
		length = (w_length + v_length)/step + 1
		width = (w_width + v_width)/step + 1
		height = (w_height + v_height)/step + 1
		
		output_matrix = np.zeros([length, width, height])

		# loop through the elements in the x direction
		for i in range(length):
			# loop throught the elements in the y direction
			for j in range(width):
				# loop throught the elements in the z direction
				for k in range(height):
					


	def convolutional_forward(self):
		pass

	def sigmoid(self):
		pass

	def sigmoid_prime(self):
		pass




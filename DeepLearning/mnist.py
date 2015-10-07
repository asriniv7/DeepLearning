#import csv
#import matplotlib
import matplotlib.pyplot as plot
import matplotlib.cm as cm  
import numpy as np
from random import shuffle


class Network(object):
	def __init__(self, sizes):
		self.num_layers = len(sizes)
		self.sizes = sizes
		self.biases = [np.random.randn(y,1) for y in sizes[1:]]
		self.weights = [np.random.randn(y,x) 
						for x,y in zip(sizes[:-1], sizes[1:])]

	def feedforward(self,a):
		for b,w in zip(self.biases,self.weights):
			a = sigmoid(np.dot(w,a)+b)
		#print a
		#print "\n"
		return a

def sigmoid(z):
	return 1.0/(1.0 + np.exp(-z))

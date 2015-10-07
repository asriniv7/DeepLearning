from numpy import genfromtxt
def load_dataset():
	filename = "train.csv"
	data = genfromtxt(filename,delimiter=',')

	labels = data[1:,0]
	train_data = data[1:,1:]

	return (train_data, labels)
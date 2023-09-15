from estimate_price import read_theta, write_theta
import numpy as np
import csv

def training():
	data = None
	correct = False
	while not correct:
		try : 
			datafile = input("please enter the path and name of the data file: ")
			with open(datafile) as f:
				data = list(csv.reader(f, ","))
			if data:
				correct = True
		except KeyboardInterrupt:
			exit()
		except:
			print("the file you tried to open was not found")
	print(data)


training()
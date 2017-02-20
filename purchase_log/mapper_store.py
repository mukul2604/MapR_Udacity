#! /usr/bin/python
import sys 

def mapper():
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) is not 6:
			continue
		date, time, store, item, cost, payment = data 
		
		print "{0}\t{1}".format(store, cost)

mapper()

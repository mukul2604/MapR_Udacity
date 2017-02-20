#! /usr/bin/python
import sys

def reducer():
	salesMax = 0
	oldKey = None

	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 2:
			continue

		thisKey, thisSale = data

		if oldKey and oldKey != thisKey:
			print "{0}\t{1}".format(oldKey, salesMax) 
			salesMax = 0

		oldKey = thisKey
		if salesMax < float(thisSale):
			salesMax = float(thisSale)

	if oldKey != None:
		print "{0}\t{1}".format(oldKey, salesMax)

reducer() 

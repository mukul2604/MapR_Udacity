#! /usr/bin/python
import sys

def reducer():
	count = 0
	salesTotal = 0
	for line in sys.stdin:
		data = line.strip().split("\t")
		if len(data) != 2:
			continue
		thisKey, thisSale = data
		salesTotal += float(thisSale)
		count += 1
	print salesTotal, count

reducer() 

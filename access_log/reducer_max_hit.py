#! /usr/bin/python
import sys

def reducer():
	hitsTotal = 0
	oldKey = None
	currentMax = 0
	path = None

	for line in sys.stdin:
		data = line.strip()
		thisKey = data

		if oldKey and oldKey != thisKey:
			if currentMax < hitsTotal:
				currentMax = hitsTotal
				path = oldKey 
			hitsTotal = 0

		oldKey = thisKey
		hitsTotal += 1

	if oldKey != None:
		hitsTotal += 1
		if currentMax < hitsTotal:
			currentMax = hitsTotal
			path = oldKey
 
	print path, currentMax
reducer() 

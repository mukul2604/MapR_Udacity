#! /usr/bin/python
import sys

def reducer():
	count = 0
	for line in sys.stdin:
		if line.strip() == '10.99.99.186':
			count += 1
	print count

reducer() 

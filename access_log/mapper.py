#! /usr/bin/python
import sys 

def mapper():
	for line in sys.stdin:
		data = line.strip().split()
		if len(data) is not 10:
			continue
		request = data[6].strip().split('http://www/the-associates.co.uk')
		
		if len(request) > 1:
			if  request[1] == '/':
				continue	
			print request[1]
		else:
			if request[0] == '/':
				continue
			print request[0]
mapper()

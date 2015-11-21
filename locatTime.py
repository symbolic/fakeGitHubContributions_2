#-*- coding:utf-8 -*- 
 
import socket 
import struct 
import time 
import win32api 
import random
import os
 
def getOfflineTime(days):
	OFFSET = 31536000L
	data_result = 1470545989
	data_result = data_result - OFFSET + days*3600*24
	return data_result
 

def setSystemTime(days): 
	tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst = time.gmtime(getOfflineTime(days))
	win32api.SetSystemTime(tm_year, tm_mon, tm_wday, tm_mday, tm_hour, tm_min, tm_sec, 0) 
	print tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst
	
	print "Set System OK!" 
	
def getRandom():
	stopNum = (int)(time.time()%100)
	print str(random.randint(0, stopNum))
	return str(random.randint(0, stopNum))
 
if __name__ == '__main__': 
	timeSpaces = 5
	
	while True:
		fp = open('random.txt', 'w')
		fp.write(getRandom())
		fp.close()
		os.system('git add .')
		os.system('git commit -m "commit"')
		
		time.sleep(timeSpaces)
		
	print 'finished'
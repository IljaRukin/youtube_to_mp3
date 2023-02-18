import csv
import sys
import os
from pytube import YouTube

failed = list()

try:
	with open('download_links.txt','r',encoding='utf-8') as f:
		url_list = f.readlines()
		numElements = len(url_list)
		for iter in range(numElements):
			print('-----'+str(iter+1)+'/'+str(numElements)+'-----')
			line = url_list.pop()
			line = line.strip('\n')
			try:
				print('downloading: ',line)
				YouTube( line ).streams.filter(only_audio=True)[0].download()
			except Exception as ex:
				print('error on: ',line)
				print(ex)
				failed.append(line)
	with open('download_links.txt','w',encoding='utf-8') as ff:
		for item in (url_list+failed):
			item = item.strip('\n')
			_=ff.write('%s\n' % item);
except KeyboardInterrupt:
	print('Interrupted')
	with open('download_links.txt','w',encoding='utf-8') as ff:
		for item in (url_list+[line]+failed):
			item = item.strip('\n')
			_=ff.write('%s\n' % item);
	sys.exit(0)

print('done \n\n')

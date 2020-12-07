from pytube import YouTube
import csv

failed = list()

#open txt
with open('download.txt','r',encoding='utf-8') as f:
	for line in f.readlines():
		line = line.strip('\n')
        #download
		try:
			print('downloading: ',line)
			YouTube( line ).streams.filter(only_audio=True)[0].download()
		except:
			print('error on: ',line)
			failed.append(line)

with open('download.txt','w',encoding='utf-8') as ff:
	for item in failed:
		_=ff.write('%s\n' % item);

print('done \n\n')
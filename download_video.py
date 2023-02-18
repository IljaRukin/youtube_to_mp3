import csv
import sys
import os
#from pytube import YouTube
from yt_dlp import YoutubeDL
ydl_opts = {
'format':' bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4',
'forcefilename':'True'
}
vid = YoutubeDL(ydl_opts)

try:
	with open('download.txt','r',encoding='utf-8') as f:
		url_list = f.readlines()
		failed = list()
		numElements = len(url_list)
		for iter in range(numElements):
			print('-----'+str(iter+1)+'/'+str(numElements)+'-----')
			line = url_list.pop()
			line = line.strip('\n')
			try:
				#YouTube( line ).streams.get_highest_resolution().download()
				print('downloading: ',line)
				vid.download(line)
				data = vid.extract_info(line)
				date = data["upload_date"]
				name = vid.prepare_filename(data)
				os.rename(name, date + '_' + name)
			except Exception as ex:
				print('error on: ',line)
				print(ex)
				failed.append(line)
	with open('download.txt','w',encoding='utf-8') as ff:
		for item in (url_list+failed):
			item = item.strip('\n')
			_=ff.write('%s\n' % item);
except KeyboardInterrupt:
	print('Interrupted')
	with open('download.txt','w',encoding='utf-8') as ff:
		for item in (url_list+[line]+failed):
			item = item.strip('\n')
			_=ff.write('%s\n' % item);
	sys.exit(0)

print('done \n\n')

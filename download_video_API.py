from pytube import YouTube
import csv

import googleapiclient.discovery
youtube = googleapiclient.discovery.build(
    "youtube", "v3", developerKey='?????'
)

failed = list()

with open('download.txt','r',encoding='utf-8') as f:
	for line in f.readlines():
		line = line.strip('\n')
        #download
		try:
			#get filename and upload date
			id_pos = line.find('watch?v=')+8
			if id_pos==7:
				id_pos = line.find('shorts/')+7
			request = youtube.videos().list(
			    part="snippet",
			    id=line[id_pos:]
			)
			response = request.execute()
			new_filename = response['items'][0]['snippet']['publishedAt']+'_'+response['items'][0]['snippet']['title']+'.mp4'
			new_filename = new_filename.replace(':','.')
			new_filename = new_filename.replace('/','_')
			new_filename = new_filename.replace('\\','_')
			new_filename = new_filename.replace('<','_')
			new_filename = new_filename.replace('>','_')
			new_filename = new_filename.replace('*','_')
			new_filename = new_filename.replace('?','_')
			new_filename = new_filename.replace('|','_')
			#download video
			print('downloading: ',line)
			YouTube( line ).streams.get_highest_resolution().download(filename=new_filename)
			#YouTube( line ).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
		except Exception as ex:
			print('error on: ',line)
			print(ex)
			failed.append(line)

with open('download.txt','w',encoding='utf-8') as ff:
	for item in failed:
		_=ff.write('%s\n' % item);

print('done \n\n')

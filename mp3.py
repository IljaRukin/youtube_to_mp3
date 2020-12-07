from os import listdir
from moviepy.editor import *

#find all mp4 files
arr = listdir()
for n in range(len(arr)-1,-1,-1):
	if arr[n][-4:]!='.mp4':
		arr.pop(n)

#convert to mp3
while len(arr)>0:
	filename = arr.pop(0)
	audioclip = AudioFileClip(filename)
	audioclip.write_audiofile(filename[:-3]+'mp3')
	print('---removing: ',filename)
	os.remove(filename)

audioclip.close()
#! python3
import time
import codecs
import datetime

link_file_name = str(datetime.date.today()) + " " + input("enter name for link file (without .txt):")
urlstart = "www.youtube.com/" #prefix
looking = "watch?v=" #word to search for

datasearch = codecs.open('website.txt','r','utf-8',errors='ignore')
linkset = set()

for line in datasearch:
	pos = 0
	try:
		counter = int(line.count(looking))
		c = 0
		for c in range(0,counter):
			pos = line.index(looking, pos)
			linkset.add(urlstart+line[pos:pos+19]+"\n")
			c += 1
	except ValueError:
		break

datasearch.close()

links = open(link_file_name+".txt","a")

print(str(len(linkset))+' links found')

full = True
while full == True:
	try:
		links.write(linkset.pop())
	except KeyError:
		full = False

links.close()


print('done')
time.sleep(5)
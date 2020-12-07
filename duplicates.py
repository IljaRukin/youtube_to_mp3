#! python3
import codecs
import time

inputed = input("enter links file name (without .txt) :")
links_file_name = str(inputed)

###get all links
datasearch = codecs.open(links_file_name+".txt",'r','utf-8',errors='ignore')
linkset = set()

i=0
for line in datasearch:
	line = line.strip('https://')
	line = line.strip('http://')
	linkset.add(line)
	i+=1

datasearch.close()

print('from',i,'links',len(linkset),'are left')

###write all links
links = open(links_file_name+".txt","a")

full = True
while full == True:
	try:
		links.write(linkset.pop().replace('\r', '').replace('\n', '')+'\n')
	except KeyError:
		full = False

links.close()

print('done')
time.sleep(5)
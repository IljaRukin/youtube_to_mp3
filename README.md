# youtube_tools_to_mp3
short scripts to collect links, remove duplicates, download videos and convert to mp3

### important note
please install the newest version of pytube for the youtube downloader to work using the following command:
```
python -m pip install git+https://github.com/nficano/pytube
```
also moviepy is required
```
pip install moviepy
```

## youtube_link_scrapper_firefox.py / youtube_link_scrapper_chrome.py
collects links from any playlist. this script opens a test enviroment, scrolls all the way down, downloads html file and extracts all video links.

## only_extract.py
this script exctracts the video links if html file was already downloaded.

## duplicates.py
removes duplicate links from a file where each link is written in a separate line

## download.py
downloads all video from links contained in a file download.txt from the same directory. links to successfuly downloaded videos are removed from download.txt , where as links of failed downloads are stored again.

## mp3.py
converts all .mp4 files in a directory to .mp3 files

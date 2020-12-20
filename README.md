# youtube_tools_to_mp3
short scripts to collect links, remove duplicates, download videos and convert to mp3

## youtube_link_scrapper_firefox.py / youtube_link_scrapper_chrome.py
collect links from any playlist. this script opens a test enviroment, scrolls all the way down, downloads html file and extracts all video links.

## only_extract.py
this script exctracts the video links if html file was already downloaded.

## duplicates.py
opens a file and removes duplicate links

## download.py
downloads all video links contained in a file download.txt from the same directory. links to successfuly downloaded videos are removed from download.txt , where as links to failed downloads are stored again.

## mp3.py
converts all .mp4 files in a directory to .mp3 files

<p style="color:red">
### important note
please install the newest version of pytube for the youtube downloader to work using the following command:<br>
python -m pip install git+https://github.com/nficano/pytube
</p>
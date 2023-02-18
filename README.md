# youtube_to_mp3
collection of scripts to collect links, remove duplicates, download video and audio and convert video to audio from youtube

### download_audio.py
download audio from youtube directly (using pytube)

### download_video.py
download video from youtube (using pytube)

### mp4_to_mp3.py
converts all .mp4 to .mp3 files (using moviepy)

### download_video_uploaddate.py
download video from youtube with uploaddate in filename (using YoutubeDL)

### download_video_API.py
download video from youtube using youtubes APIv3 (using googleapiclient)
first you need to enter your Key to do so

### youtube_link_scrapper_firefox.py / youtube_link_scrapper_chrome.py
collects links from any playlist. this script opens a test enviroment, scrolls all the way down, downloads html file and extracts all video links.

### only_extract.py
this script exctracts the video links from html file

### remove_duplicates.py
removes duplicate links from a file where each link is written in a separate line

### important note
please install the newest version of pytube, moviepy, YoutubeDL and googleapiclient
```
python -m pip install git+https://github.com/pytube/pytube
pip install moviepy
pip install yt-dlp
pip install google-api-python-client
```

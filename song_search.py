from bs4 import BeautifulSoup
import requests
import webbrowser
import time
from subprocess import call

base_url="https://www.youtube.com"		

def download_song(url):
           
        #req = urllib2.Request(url,headers=hdr)
        req = requests.get(url)
        homePageSoup = BeautifulSoup(req.content,'html.parser')
        vid=homePageSoup.find(attrs={'class':'yt-lockup-title '})
        final_url=base_url+vid.a['href']
        call(['youtube-dl',"-x","--extract-audio","--audio-format","mp3",final_url])
             
def song_dowload():
	name=raw_input("Enter song name ")
	
	download_song("https://www.youtube.com/results?search_query="+name)

def artist_download(artist_name):
	artist_name = artist_name.replace(" ", "%20")
	url = "http://www.top50songs.org/artist.php?artist=" + artist_name
	soup = BeautifulSoup(requests.get(url).text, "html.parser")
	artist_songs=[]
	k=0
	for link in soup.findAll('a'):
		
		href = link.get("href")
		song_name = link.get("title")
		
		if(href != None and "/song-info/" in href):
                    #k=k+1
                    artist_songs.append(str(k)+" "+song_name)
                    k=k+1
	for j in artist_songs:
		print j		
	ch = int(raw_input("Enter the index of song "))
	print "Fetching song"	
	download_song("https://www.youtube.com/results?search_query="+artist_songs[ch])

choice = int(raw_input("Press 1 to search by name or 2 to search by artist: "))
if choice==1:
	song_dowload()
else:
    artist_choice = raw_input("Enter the name of the artist you'd like to get songs from: ")
    artist_download(artist_choice)

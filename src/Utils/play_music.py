#Play music on yt
import os
import sys
import requests
import re
from bs4 import BeautifulSoup
sys.path.append(".")
sys.path.append("./")
sys.path.append("../")
import requests
from src.Utils.open_website import OpenWebsite
from bs4 import BeautifulSoup
def open_music_with_yt(song_name:str):
    url1 = ""
    song_name = song_name.lower()
    url = "https://www.google.com/search?q=" + "+".join(song_name.split(" "))
    print(url)
    headers = {'User-Agent':'Mozilla/5.0'}
    soup = BeautifulSoup(requests.get(url,headers=headers).text,features="html.parser")
    print(soup.prettify())
    links = soup.find_all("div",class_="BNeawe tAd8D AP7Wnd")
    for link in links:
        if bool(re.search("youtube.com/watch",link.text)):
            url1 = link.text
            print(url1)
    if(len(url1)>0):
        print(url1)
        OpenWebsite().open_browser_with_url(url1)
    else:
        print("Cant find music + {}".format(song_name.replace("","+")))
    

if __name__ == "__main__":
    open_music_with_yt("Maybe I")
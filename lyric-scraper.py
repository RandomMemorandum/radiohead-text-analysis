from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import re
import requests
import urllib3

radiohead_url = 'https://www.azlyrics.com/r/radiohead.html'

response = requests.get(radiohead_url)

html_content = response.text

# scrape song names, albums, relevant dates
# identify what html elements contain the links for each song
# find links for each song page
# execute hyper link for each song
# identify elements containing lyrics
# copy lyrics
# output file containing

soup = BeautifulSoup(html_content, 'html.parser')

# getting song titles and hyperlinks to each lyric page
domain = 'https://www.azlyrics.com'
song_link_list = [['Page','URL']]
for line in soup.find_all('a'):
    row = []
    song_title = line.text
    url = re.findall("/.*\.html", str(line))
    if len(url) < 1: continue
    row.append(song_title)
    row.append(domain + url[0])
    song_link_list.append(row)

# gathering album names
# find div tag where class = album, get name and year
album_names = [['release_type','title','year']]
album_lines = soup.find_all(class_='album')
for line in album_lines:

    row = line.text.split('"')

    if len(row) < 3: continue

    row[0] = row[0].strip().strip(':')
    row[2] = row[2].strip(' ()')
    album_names.append(row)







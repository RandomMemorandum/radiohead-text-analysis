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




from bs4 import BeautifulSoup
import requests
import sys
import time

url = sys.argv[1]

response = requests.get(url)
	
# === getting song metadata ===
soup = BeautifulSoup(response.text, 'html.parser')

metadata = []
for detail in soup.find_all('b'):
    metadata.append(detail.text)

band = metadata[0].split()[0]
song = metadata[1].strip('"').replace(' ','')
album = metadata[2].strip('"').replace(' ','')

# === reading a slice of the HTML doc to get lyrics ===
lyrics_div_loc = response.text.index('div class="lyricsh"')
noprint_div_loc = response.text.index('div class="noprint"')
clipped_response = response.text[lyrics_div_loc:noprint_div_loc]

soup = BeautifulSoup(clipped_response, 'html.parser')

divs = soup.find_all('div')

# === wrapup ===
localtime = time.asctime(time.localtime(time.time()))
localtime_list = localtime.split()

year = localtime_list[4]
month = localtime_list[1]
day = localtime_list[2]
time_now = localtime_list[3].replace(':','%')

filename = '{}-{}-{}-{}-{}-{}-{}.txt'.format(band,album,song,year,month,day,time_now)

with open(filename, "w") as f:
    for line in divs:
        f.write(line.text.strip())



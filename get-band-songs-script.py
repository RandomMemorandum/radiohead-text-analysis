from bs4 import BeautifulSoup
import csv
import re
import requests
import sys
import time

band_name = sys.argv[1]

start_letter = band_name[0]
contracted_band_name = band_name.replace(' ', '')

url = 'https://www.azlyrics.com/{}/{}.html'.format(start_letter, contracted_band_name)

try:
    response = requests.get(url)
except: print("No results found")

html_content = response.text
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

# ===== gathering album names =====
album_names = [['release_type','title','year']]
album_lines = soup.find_all(class_='album')
for line in album_lines:

    row = line.text.split('"')

    if len(row) < 3: continue

    row[0] = row[0].strip().strip(':')
    row[2] = row[2].strip(' ()')
    album_names.append(row)

# ===== writing all results to file =====
localtime = time.asctime(time.localtime(time.time()))
localtime_list = localtime.split()

year = localtime_list[4]
month = localtime_list[1]
day = localtime_list[2]
time_now = localtime_list[3].replace(':','.')

band = contracted_band_name

filename = '{}-songs-{}-{}-{}-{}.csv'.format(band,year,month,day,time_now)

with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerows(song_link_list)
f.close()


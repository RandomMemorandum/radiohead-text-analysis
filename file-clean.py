import collections
import numpy as np
import pandas as pd
import sys

file = sys.argv[1]
#==========================================================================
metadata = {}
metadata['track_no'] = file.split('-')[0]
metadata['band'] = file.split('-')[1]
metadata['album'] = file.split('-')[2]
metadata['track_name'] = file.split('-')[3].split('.')[0]
#==========================================================================

with open(file, 'r') as f:
    lines = f.readlines()

words = {}
word_list = []

for line in lines:
    line = line.strip()
    for word in line.split(' '):
        if len(word) > 0:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
                
#==========================================================================

word_container = []
for key, value in words.items():
    word_container.append((value, key))
    
word_container.sort(reverse=True)

file_name = '{}-{}-summary.txt'.format(metadata['track_name'],metadata['band'])
f = open(file_name, 'w')
f.write('========================================' + '\n')
f.write('Song: ' + metadata['track_name'] + '\n')
f.write('Artist: ' + metadata['band'] + '\n')
f.write('Album: ' + metadata['album'] + '\n')
f.write('Track: ' +  metadata['track_no'] + '\n')
f.write('========================================' + '\n')
f.write('\n')
f.write('count' + '\t' + '|' + '\t' + 'word' + '\n')
f.write('----------------------------------------' + '\n')
for key, value in word_container:
    f.write(str(key) + '\t' + '|' + '\t' + value + '\n')

f.close()
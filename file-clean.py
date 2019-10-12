import numpy as np
import pandas as pd
import sys

file = sys.argv[1]

metadata = {}
metadata['track_no'] = file.split('-')[0]
metadata['band'] = file.split('-')[1]
metadata['album'] = file.split('-')[2]
metadata['track_name'] = file.split('-')[3].split('.')[0]


with open(file, 'r') as f:
    lines = f.readlines()

words = {}
word_list = []

for line in lines:
    line = line.strip()
    for word in line.split(' '):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1



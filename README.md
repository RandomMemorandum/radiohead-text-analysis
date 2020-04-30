
## Radiohead Lyrics text analysis

### Summary

This project stands as an exercise in collecting text data, manipulating it, parsing it, storing it, and finally generating summary reports and visualizing certain aspects of the text. 

Currently it uses the python libraries (in alphabetical order):  

  * BeauitfulSoup  
  * numpy  
  * pandas  
  * requests
  * sys
  * time

### Programming Steps

  Scrape raw data / lyrics from website and save as file  
  * Connect to URL
  * Read main page to get artist, albums, song titles and write to file
  * Extract hyperlinks for each song
  * Loop through list and execute hyperlinks
    * For each link, scrape title and lyrics
    * Write to its own file, following naming convention  

  Read file and parse metadata and raw data  
  * Extract needed information from file name and content of file
  * Parse information, format, and write to new clean file

  Read clean files to aggregate into single source, such as a database

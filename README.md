# Video series downloader
###### Python scripts to download embedded video podcasts by scrapping their source from webpages.

### Motivation
youtube-dl is an awesome application to download video and playlists from many sites.
But many online Video tutorials use embedded videos on different webpages rather than in the form of a playlist which cannot be handled by it or similar applications.  

So, when I needed to download the Laracast series, I came up with a simple script which loops through the URLs on the website,
searches the source link of the embedded video (using regular expression) and downloads it using 'youtube-dl' application.
  
### Using the project

1. The code supports both Python 2 and 3.
2. Dependencies:
  * youtube-dl (An application to download videos and playlists)  
  Install it by running ```sudo apt-get install youtube-dl``` on Linux  
  (See [rg3.github.io/youtube-dl/] for more info on it)
3. Clone/download the repository.  
4. Run this command in terminal:  
  ```
  python laracasts.py <starting page no.> <ending page no.>
  ```  
  For example, run ```python laracasts.py 1 27``` to download all 27 videos of Laracast series.
  
### For developers
* A script similar to ```laracasts.py``` can be written for other series also.
* ```general.py``` contains some common functions which can be used in these other scripts as well.
* The current script loops through the URLs which follow the form: base URL followed by a number.  
Hence, the script would require some modification in the loop structure as well as input format to handle URLs containg text instead of just numbers.  
* Please feel free to add scripts for other websites using the ```laracasts.py``` as reference for design.
* Besides, I have left the work of downloading a video from a direct link on ```youtube-dl``` as it can resume the download properly even after an interrupt or network error.
I would love to hear about any better way to do the final downloading step. 

## About the project author
#### Nitish Garg
B.Tech undergraduate (Computer Science & Engineering)  
IIT Guwahati  
India  

nitish.garg.6174@gmail.com  
www.linkedin.com/in/nitish6174

[rg3.github.io/youtube-dl/]: <//rg3.github.io/youtube-dl>

from __future__ import print_function	# To support print() function in older versions
import sys
import os
import subprocess

### Function to check for Python version in order to handle different syntax
def pyVersion():
	return int(sys.version_info[0])

### Importing library according to Python version
if pyVersion()<3:
	from urllib2 import urlopen
else:
	from urllib.request import urlopen

### Function to get HTML markup of a URL
def getHTML(url):
	response = urlopen(url)
	if pyVersion()<3:
		htmlSource = response.read()
	else:
		htmlSource = response.read().decode("utf-8")
	response.close()
	return htmlSource

### Function to open a video in specified browser
def openInBrowser(video_url,browser="google-chrome"):
	cmd = browser + " " + video_url
	os.system(cmd)

### Function to print the command currently being executed
def printCommand(cmd):
	# if pyVersion()<3:
		# print "Currently running : ",cmd
	# else:
	print("Currently running : " + cmd)

### Function to download the videos one-by-one
def saveSerially(file_name,video_url):
	cmd = "youtube-dl --output "+file_name+" "+video_url
	printCommand(cmd)
	os.system(cmd)

### Function to download the videos parallely
def saveParallely(file_name,video_url,last=False):
	cmd = "youtube-dl --output "+file_name+" "+video_url
	printCommand(cmd)
	if last==True:
		subprocess.call(cmd, shell=True)
	else:
		subprocess.call(cmd + " & ", shell=True)
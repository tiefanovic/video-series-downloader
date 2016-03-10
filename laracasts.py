from __future__ import print_function	# To support print() function in older versions
import sys
import re
from general import *

def main():

	### Checking correct usage
	if len(sys.argv)!=3:

		print("Usage:\n")
		print("Give command as:\n\tpython laracasts.py <starting page no.> <ending page no.>\n")
		print("Example command:\n\tpython laracasts.py 1 27\n\t(This will download all 27 videos of Laracast series)")

	else:

		first = int(sys.argv[1])
		last = int(sys.argv[2])

		### Looping through the range specified by command
		for i in range(first,last+1):

			url = "https://laracasts.com/series/laravel-5-fundamentals/episodes/"+str(i)

			htmlSource = getHTML(url)					# Function from general.py
			video_url = getVideoURL(htmlSource)
			video_title = getVideoTitle(htmlSource)

			### Name with which file will be saved
			file_name = "\"laracasts/"+str(i)+" - "+video_title+".mp4\""

			### Uncomment below line to open the video URL in browser (browser name is optional and set for chrome by default)
			# openInBrowser(video_url,"firefox")

			### Running the function from general.py which saves the videos parallely
			if i==last:
				saveParallely(file_name,video_url,True)
			else:
				saveParallely(file_name,video_url)

			### Alternately, videos can be saved serially by the following code
			# saveSerially(file_name,video_url)


### Following functions are specific to the HTML code pattern on site
### May need modification if site's source code is changed in the future

### Returns video URL from the source code
def getVideoURL(htmlSource):
	regex_video = r"source src=\"([^\"]+)"
	result_video = re.findall(regex_video,htmlSource)
	video_url = "https:"+result_video[0]
	return video_url

### Returns video title from the source code
def getVideoTitle(htmlSource):
	regex_title = r"<title>([^<]+)</title>"
	result_title = re.findall(regex_title,htmlSource)
	video_title = result_title[0]
	### Replacing any '/' found in title name as it is invalid for filename
	### Other illegal characters also need to be replaced
	video_title = video_title.replace('/','-')
	return video_title


### Launching the main program
main()
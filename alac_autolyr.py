"""
	Usage:
		autolyr -R <file or dir name>
"""

import sys
import fnmatch
import os
import urllib
import urllib2
from mutagen.mp4 import MP4
from bs4 import BeautifulSoup

recursive = False
for i in sys.argv:
	if i == '-R':
		recursive = True
		break

arg = sys.argv[-1]

cat = False
if os.path.isdir(arg):
	cat = True

if not cat and not os.path.isfile(arg):
	print ("File not found: " + arg)
	sys.exit()

if not cat:
	songs = [arg]
elif recursive:
	songs = []
	for root, dirnames, filenames in os.walk(arg):
		for filename in fnmatch.filter(filenames, '*.m4a'):
			songs.append(os.path.join(root, filename))
else:
	songs = [filename for filename in fnmatch.filter(os.listdir(arg), '*.m4a')]		

print 'Found: '
for i in songs:
	print i
print

for song in songs:
	try:
		audiofile = MP4(song)

		artist = audiofile['\xa9ART'][0]
		track = audiofile['\xa9nam'][0]

		print artist + ' - ' + track
		name = urllib.quote_plus(unicode(artist).encode('utf8') + ' ' + unicode(track).encode('utf8') + ' lyrics')
		
		url = 'http://www.google.com/search?q=' + name
		req = urllib2.Request(url, headers={'User-Agent' : "foobar"})
		response = urllib2.urlopen(req)

		s = response.read()
		s = unicode(s, errors='replace')
		result = s.encode('utf8')

		link_start = result.find('http://www.metrolyrics.com')
		link_end = result.find('html',link_start + 1)

		link = result[link_start:link_end+4]
		if link == '':
			print 'Not found\n'
			continue
		lyrics_html = urllib2.urlopen(link).read()
		soup = BeautifulSoup(lyrics_html)
		raw_lyrics= (soup.findAll('p', attrs={'class' : 'verse'}))
		paras = []
		test1 = unicode.join(u'\n',map(unicode,raw_lyrics))

		test1 = (test1.replace('<p class="verse">','\n'))
		test1 = (test1.replace('<br/>',' '))
		test1 = test1.replace('</p>',' ')
		audiofile['\xa9lyr'] = [test1]
		audiofile.save()
		print('Lyrics added\n')

	except Exception as inst:
		print ('An error occured for ' + song)		
		print type(inst)
		print inst

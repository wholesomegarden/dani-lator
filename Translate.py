# -*- coding: utf-8 -*-

# This simple app uses the '/translate' resource to translate text from
# one language to another.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

import os, requests, uuid, json
import lyricwikia


#gen.py


# Make HTTP requests
import requests
# Scrape data from an HTML document
from bs4 import BeautifulSoup
# I/O
import os
# Search and manipulate strings
import re

# class gen:
GENIUS_API_TOKEN = client_access_token = 'q2iKacoJeJRs5q6UC1AnYWN4IriZnwgV4FhoXWxIERxORuOb9GxUdAbWDD_K1D5q'


item = "stairway to heaven"
# item = input('Enter the song to find its lyrics: ')


import requests
from bs4 import BeautifulSoup, UnicodeDammit
# import datetime
def gsearch(item):
	searchSong='https://www.google.com/search?q='
	# s=input('Enter the song to find its lyrics: ')
	s = '\"'+item+'\"'

	#calculating time taken in searching lyrics
	# a = datetime.datetime.now()
	for i in s:
		if i==' ':
			searchSong+='+'
		else:
			searchSong+=i
	searchSong+='+lyrics'



	headers_Get = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'DNT': '1',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1'
		}



	searchPage = requests.get(searchSong, headers=headers_Get)
	html = BeautifulSoup(searchPage.text,'html.parser')
	lyrics=html.find_all("span", jsname="YS01Ge")
	if lyrics==[]:
		print('Couldn\'t get lyrics')
	else:
		nlyr = ""
		nl = [", ","\n"]
		c = 0
		for i in lyrics:
			# print(i.get_text())
				nlyr += i.get_text() + nl[c%2]
				c+=1
		return nlyr


# Get artist object from Genius API
def request_artist_info(artist_name, page):
	base_url = 'https://api.genius.com'
	headers = {'Authorization': 'Bearer ' + GENIUS_API_TOKEN}
	search_url = base_url + '/search?per_page=10&page=' + str(page)
	data = {'q': artist_name}
	response = requests.get(search_url, data=data, headers=headers)
	return response
# Get Genius.com song url's from artist object
def request_song_url(artist_name, song_cap):
	page = 1
	songs = []

	while True:
		response = request_artist_info(artist_name, page)
		json = response.json()
		# Collect up to song_cap song objects from artist
		song_info = []
		for hit in json['response']['hits']:
			if artist_name.lower() in hit['result']['primary_artist']['name'].lower():
				song_info.append(hit)

		# Collect song URL's from song objects
		for song in song_info:
			if (len(songs) < song_cap):
				url = song['result']['url']
				songs.append(url)

		if (len(songs) == song_cap):
			break
		else:
			page += 1

	print('Found {} songs by {}'.format(len(songs), artist_name))
	return songs

# DEMO
# print("!!!!!!",request_song_url('Lana Del Rey', 2))

# Scrape lyrics from a Genius.com song URL
def scrape_song_lyrics(url):
	page = requests.get(url)
	html = BeautifulSoup(page.text, 'html.parser')
	lyrics = html.find('div', class_='lyrics').get_text()
	print(lyrics)
	#remove identifiers like chorus, verse, etc
	lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
	#remove empty lines
	lyrics = os.linesep.join([s for s in lyrics.splitlines() if s])
	return lyrics
# DEMO
# print(scrape_song_lyrics('https://genius.com/Lana-del-rey-young-and-beautiful-lyrics'))


def searchLyrics(search, res = 1):
	urls = request_song_url(search, res)
	return scrape_song_lyrics(urls[0])


# lyrics = lyricwikia.get_lyrics('Led Zeppelin', 'Stairway to heaven')
# from search import *

# import urllib2
# from urllib.request import urlopen
# import ssl


# from urllib.request import Request, urlopen
# x = "https://www.google.com/search?q=hello+lyrics"
# req = Request(x, headers={'User-Agent': 'Mozilla/5.0'})



# webpage = urlopen(req).read()

# print(webpage)
# ssl._create_default_https_context = ssl._create_unverified_context

# html = urlopen(x).read()
# print(html)
print("")
print("")
print("")

GCS_API_KEY = 'AIzaSyCHOkya9h3n7BWA10S_CQQkz-p9Wlreh44'
GCS_ENGINE_ID = 'Danilator'
# from lyrics_extractor import SongLyrics


def getLyrics(title):
	# return lyricwikia.get_lyrics('Led Zeppelin', 'Stairway to heaven')
	# search("")
	# print("title",title)
	lyrics = gsearch(title)
	# print(lyrics)

	# print()
	# print("!!!!!!!")
	return lyrics


	item = "stairway to heaven"

	lyrics = searchLyrics(item)
	return lyrics

	extract_lyrics = SongLyrics(GCS_API_KEY)

	data = extract_lyrics.get_lyrics("Shape of You")

#     return '''
#     There's a lady who's sure all that glitters is gold
# And she's buying a stairway to heaven
# And when she gets there, she knows if the stores are all closed
# With a word she can get what she came for
#
# Oohoohooh oohoohoohoohooh
#
# And she's buying a stairway to heaven
#
# There's a sign on the wall but she wants to be sure
# 'Cause you know sometimes words have two meanings
# In a tree by the brook there's a songbird that sings
# Sometimes all of our thoughts are misgiven
#
# And I think you can see that
#
# Ohh
#
# [Chorus]
# And it makes me wonder, sure does
# Oh hoh hoh, hohooh ohoohohooh, yes sir
#
# [Verse 2]
# There's a feelin' I get when I look to the west
# And my spirit is crying for leaving
# In my thoughts I have seen rings of smoke through the trees
# And the voices of those who stand looking
#
# Ah hah. Ah hah
# Ah hah. Ah hah. Ahhhahhohoohohooh
#
# [Verse 3]
# And it's whispered that soon if we all call the tune
# Then the piper will lead us to reason
# And a new day will dawn for those who stand long
# And the forests will echo with laughter
#
# Does anybody remember laughter?
#
# Baby! Oh, baby look...
# Just give it to me, give it to me, give it to me
#
# Sure does, sure does
#
# But I got some good news, listen...
#
# [Verse 4]
# If there's a bustle in your hedgerow, don't be alarmed now
# It's just a spring clean for the May queen
# Yes, there are two paths you can go by, but in the long run
# There's still time to change the road you're on
#
# I hope so
#
# Oohh! Baby, baby, baby
# Ya, darlin' babe
# Ya, darlin' babe
# Ya, darlin' babe
#
# Wait a minute...
#
# [Verse 5]
# Your head is hummin' and it won't go in case ya don't know
# The piper's callin' you to join him
# Dear Lady, can you hear the wind blow and did you know
# Your stairway lies on the whisperin' wind?
#
# Ohh hah hahhahhh
#
# [Guitar Solo]
#
# [Bridge]
# And as we wind on down the road
# Our shadows taller than our souls
# There walks a lady we all know
# Who shines white light and wants to show
# How everything still turns to gold, yeah
# And if you listen very hard
# The tune will come to you at last
# When all is one and one is all
# To be a rock and not to roll, not to roll
#
# [Outro]
# And she's buying a stairway to heaven
# Ahhahhhhohhahhoh
#     '''
#     return '''
#     Angels on the sideline
# Puzzled and amused
# Why did Father give these humans free will?
# Now they're all confused
# Don't these talking monkeys know that Eden has enough to go around?
# Plenty in this holy garden, silly old monkeys
# Where there's one you're bound to divide it
# Right in two
# Angels on the sideline
# Baffled and confused
# Father blessed them all with reason
# And this is what they choose
# Monkey killing monkey killing monkey over pieces of the ground
# Silly monkeys give them thumbs
# They forge a blade, and where there's one they're bound to divide it
# Right in two
# Right in two
# Monkey killing monkey killing monkey over pieces of the ground
# Silly monkeys give them thumbs, they make a club
# And beat their brother down
# How they survive so misguided is a mystery…
#     '''


key_var_name = '6e212400769e4218b93a53e51f3893cf'
# if not key_var_name in os.environ:
#     raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = '6e212400769e4218b93a53e51f3893cf'

endpoint = "https://api.cognitive.microsofttranslator.com/"

# If you encounter any issues with the base_url or path, make sure
# that you are using the latest endpoint: https://docs.microsoft.com/azure/cognitive-services/translator/reference/v3-0-translate
path = '/translate?api-version=3.0'
params = '&to=he'
constructed_url = endpoint + path + params

headers = {
	'Ocp-Apim-Subscription-Key': subscription_key,
	'Content-type': 'application/json',
	'X-ClientTraceId': str(uuid.uuid4())
}

# You can pass more than one object in body.



def doit():
	item = input('Enter the song to find its lyrics: ')
	lyricsText = getLyrics(item)
	chars = [["-"," "],["(",""],[")",""]]
	for c in chars:
		lyricsText = lyricsText.replace(c[0],c[1])
	# .replace().replace("(","").replace(")","")
	lyrics = []
	for l in lyricsText.split("\n"):
		lyrics.append(l)


	body = [{
		'text' : lyricsText
	}]
	request = requests.post(constructed_url, headers=headers, json=body)
	response = request.json()

	translated = []

	for r in response[0]['translations'][0]['text'][::-1].split("\n")[::-1]:
		# print(r)
		translated.append(r)




	# print("!!!!!")
	for c in range(len(translated)):
		print(lyrics[c])
		print(translated[c])
		print("")
doit()

# print(len(translated))
# print(len(lyrics))


# print()
# print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': ')))
#
#
# print(json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))[0]["translations"])

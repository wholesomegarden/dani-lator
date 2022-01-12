# -*- coding: utf-8 -*-

# This simple app uses the '/translate' resource to translate text from
# one language to another.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

import os, requests, uuid, json
# import lyricwikia


#gen.py
from youtube_title_parse import get_artist_title


# Make HTTP requests
import requests
# Scrape data from an HTML document
# from bs4 import BeautifulSoup
# I/O
import os
# Search and manipulate strings
import re

# class gen:
# GENIUS_API_TOKEN = client_access_token = 'q2iKacoJeJRs5q6UC1AnYWN4IriZnwgV4FhoXWxIERxORuOb9GxUdAbWDD_K1D5q'


# item = input('Enter the song to find its lyrics: ')


import requests
from bs4 import BeautifulSoup, UnicodeDammit, NavigableString

# from googletrans import Translator

from google_trans_new import google_translator

translator = google_translator()

from lyricsgenius import Genius
token = "pq_DFKQQcMYGRmEAXT-hxcR1FfMma3lREuGJ2DQeRry3a7q7WAHm-fxzDMooyXpA"
genius = Genius(token)

# translator = Translator()
# import datetime
#

# GCS_API_KEY = 'AIzaSyCHOkya9h3n7BWA10S_CQQkz-p9Wlreh44'
# GCS_ENGINE_ID = 'Danilator'
# from lyrics_extractor import SongLyrics

def research(url):
	html = getHTML(url)
	c = 0
	for d in html.findAll("div"):
		print(d.text)
		print(c)
		c += 1
		input()

def getHTML(url):
	headers_Get = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:77.0) Gecko/20100101 Firefox/77.0',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'DNT': '1',
	'Connection': 'keep-alive',
	'Upgrade-Insecure-Requests': '1'
	}
	# headers_Get = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}
	proxies = {
    "https": "http://178.155.104.84:59071",
    "http": "http://178.155.104.84:59071"
	}
	proxies = {
    "https": "http://51.161.130.93:8080",
    "http": "http://51.161.130.93:8080"
	}
	searchPage = requests.get(url, headers=headers_Get,proxies=proxies)
	html = BeautifulSoup(searchPage.text,'html.parser')
	return html

# research(url)

def getLyrics(title):
	song = genius.search_song(title)
	fulltitle = f"{title} / "
	lyrics = []
	if song is not None:
		fulltitle = f"{song.title} / {song.artist}"
		lyrics = song.lyrics.split("\n")[:-6]


	if lyrics==[]:
		print('Couldn\'t get lyrics')
	else:
		nlyr = ""
		# nl = ["; ","\n"] # double lined
		nl = ["\n","\n"]
		c = 0
		for i in lyrics:
			# print(i.get_text())
			if len(i.strip()) == 0 or (i.strip()[0] is not "[" and i.strip()[-1] is not "]"):
			# if True:
				nlyr += i + nl[c%2]
				c+=1
		return nlyr, fulltitle.split("/")
		return nlyr, song_info

def getLyricsGoogle(title):
	# return lyricwikia.get_lyrics('Led Zeppelin', 'Stairway to heaven')
	# search("")
	# print("title",title)
	url='https://www.google.com/search?q='
	# s=input('Enter the song to find its lyrics: ')
	s = '\"'+title+'\"'

	#calculating time taken in searching lyrics
	# a = datetime.datetime.now()
	for i in s:
		if i==' ':
			url+='+'
		else:
			url+=i
	url+='+lyrics'



	html = getHTML(url)
	# print("\n#####",html,"\n###########")
	fulltitle = f"{title} / "
	try:
		fulltitle = html.findAll("div",{"class":"kCrYT"})[0].find_all("span")[0].findParent().text
	except:
		pass
	'''
	song_info = []
	song_title = []
	for paper in html.findAll("div",class_="auw0zb"):
		for desc in paper.descendants:
			print("DDDDDDDD",desc)
		info = [desc.strip() for desc in paper.descendants if type(desc) == NavigableString]
		for i in info:
			song_title.append(i)
	print("\n#####333333",song_title,"\n###########")
	if len(song_title) > 1:
		songtitle = song_title[1].split(" lyrics ©")[0]
		song_info.append(songtitle)
	artists = []
	for paper in html.findAll("div",class_="wx62f PZPZlf x7XAkb"):
		for desc in paper.descendants:
			print("DDDDDDDD",desc)
		info = [desc.strip() for desc in paper.descendants if type(desc) == NavigableString]
		for i in info:
			artists.append(i)
	print("\n#####",artists,"\n###########")
	if len(artists) > 0:
		artist = artists[0].replace("Song by ","")
		song_info.append(artist)

	if len(song_info) < 2:
		print("wwwwwwwwwwww",song_info)
		song_info = []
		# for paper in html.findAll("div",class_="SPZz6b"):
		for paper in html.findAll("div[class*=wwUB2c]"):
			for desc in paper.descendants:
				print("DDDDDDDD",desc)
			info = [desc.strip() for desc in paper.descendants if type(desc) == NavigableString]
			for i in info:
				song_info.append(i)
	'''

	# lyrics=html.find_all("span", jsname="YS01Ge")
	# lyrics=html.find_all("span", jsname="YS01Ge")
	lyrics=html.find_all("div", {"class":"hwx"})
	# lyrics=html.find_all("div", {"class":"hwx"})[0].findParent()
	if lyrics==[]:
		print('Couldn\'t get lyrics')
	else:
		nlyr = ""
		nl = ["; ","\n"]
		c = 0
		for i in lyrics:
			# print(i.get_text())
				nlyr += i.get_text() + nl[c%2]
				c+=1
		return nlyr, fulltitle.split("/")
		return nlyr, song_info

def changes(txt,dict):
	for k in dict:
		txt = txt.replace(k,dict[k])
	return txt

def chunks(lst, n):
	"""Yield successive n-sized chunks from lst."""
	for i in range(0, len(lst), n):
		yield lst[i:i + n]


def doit(item):
	if item == "":
		return "", ["",""]
		# item = input('Enter the song to find its lyricsxx: ')

	res = None
	maxTries = 4
	mc = 0
	lyricsText, song_info = "sorry, lyrics not found, try again soon ",["Could not find lyrics",item]
	while res is None and mc <= maxTries:
		# try:
		target = item
		print("ITEM:"+target)
		artist_title = get_artist_title(target)
		if artist_title is not None:
			print("@@@@@@@@@@@@@@@@@@@@",artist_title)
			artist, title = artist_title

			if mc==1:
				target = title+" " + artist
				item = item.replace("&"," and ")
			if mc==2:
				target = title+" " + artist.split(" ")[0]
			if mc==3:
				target = title
		else:
			print("!!!!!!!!!!!!!!!!!!!!!!!!")
			print("!!!!!!!!!!!!!!!!!!!!!!!!")
			print("!!!!!!!!!!!!!!!!!!!!!!!!")

		print("TTTTTTTTTTTTTTTTT")
		print(target)
		print("TTTTTTTTTTTTTTTTT")
		# except:
		# 	print("E: could not parse artist and title")
		res = getLyrics(target)
		mc+=1
		if res is not None and len(res) > 1:
			lyricsText, song_info = res

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

	translated = []
	debug = False
	bing = False
	if bing:
		request = requests.post(constructed_url, headers=headers, json=body)
		response = request.json()

		fullL = []

		i = 0
		print()
		print("!!!!!!!!!",response)
		print()


		if type(response) == type({}) and "error" in response.keys():
			if response["error"]["code"] != "0":
				print("EEEEEE")
				print("EEEEEE")
				print("EEEEEE")
				song_info.append(""+str(response))
		else:
			print(c)
			for r in response[0]['translations'][0]['text'][::-1].split("\n")[::-1]:
				print("@@@@@@@",r)

				# fullL = [lyrics[i]+"\n"+r[::-1]]
				translated.append(r)
				i+=1
	else:

		n = 0
		parts = []
		print(lyricsText)
		print(type(lyricsText), len(lyricsText),len(lyricsText.split("\n")))
		maxChunks = 50
		for chunk in chunks(lyricsText.split("\n"), maxChunks):
			match = False
			joiner = " øxø"
			joiner = " █"
			joiner = " ø"
			finalJoiner = ""
			joiners = [" øxø"," AAAAA"," øø"," █"]
			joiners = [" øøø "," øxø"]
			joiners = [" 123\n "," øxø\n"]
			# joiners = [" 123\n "]
			res = ""
			for joiner in joiners:
				if not match:
					finalJoiner = joiner
					# joiner = " █ øxø"
					# joinerN = joiner+"\n"
					joinerN = joiner
					chunkT = joinerN.join(chunk)
					print("!!!!!!!!!!!!","\n",chunkT) #XXX
					# res = translator.translate(str(chunkT),lang_tgt="he").replace("Ø","ø").replace(joinerN,joiner.strip())
					res = translator.translate(str(chunkT),lang_tgt="he").replace("Ø","ø")#.replace(joinerN,joiner.strip())
					if chunkT.count(joiner.strip().strip("\n")) == res.count(joiner.strip().strip("\n")):
						match = True
						if debug:
							res += f"--- "+str(chunkT.count(joiner.strip().strip("\n")))+" ======== "+str(res.count(joiner.strip().strip("\n")))
					else:
						print(f"--- "+str(chunkT.count(joiner.strip().strip("\n")))+" != "+str(res.count(joiner.strip().strip("\n"))))
						if debug:
							res += f"--- "+str(chunkT.count(joiner.strip().strip("\n")))+" != "+str(res.count(joiner.strip().strip("\n")))
			if len(res.split("\n")) > 1:
				res=res.replace(finalJoiner.strip(),"")
			else:
				if debug:
					res=res.replace(finalJoiner.strip(),"@@\n")
				else:
					res=res.replace(finalJoiner.strip(),"\n")
			if debug:
				res+=f"~~~ line count"+str(len(res.split("\n")))
			print("$$$$$$$$$$$$$$$$$$$$$")
			print(res)
			parts.append(res.replace("OXO",""))
		# time.sleep(1)
			# n+=1
		# res = translator.translate(lyricsText,lang_tgt="he")
		print("########################@@@")
		print(parts)
		# translated = res.__dict__()["text"]
		translated = ("\n".join(parts)).split("\n")
		print("############################")
		print(translated)
		print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")

		# replacements = {" ":"%20", ";":"%3B", "\n":"%0A", ",":"%2C","\'":"%27"}
		# base = "https://translate.google.com/?sl=auto&tl=iw&text="
		# ending = "&op=translate"
		#
		# print(lyricsText)
		# # input()
		# url = base + changes(lyricsText, replacements) + ending
		#
		# print(url)
		#
		# page = requests.get(url)
		# soup = BeautifulSoup(page.content, 'html.parser')
		#
		# spans = soup.find_all("span")
		# #
		# # for pp in P:
		# # 	lyrics.append(pp.text.replace("\n","").replace("                ","").replace("              ",""))
		#
		# for s in spans:
		# 	print(":::: ",s.text)
		# 	translated.append(s.text)


		# response = request.json()

		# https://translate.google.com/?sl=auto&tl=iw&text=She%27s%20got%20a%20smile%20that%20it%20seems%20to%20me%0AReminds%20me%20of%20childhood%20memories%0AWhere%20everything%20was%20as%20fresh%20as%20the%20bright%20blue%20sky%0ANow%20and%20then%20when%20I%20see%20her%20face%0AShe%20takes%20me%20away%20to%20that%20special%20place%0AAnd%20if%20I%20stare%20too%20long%2C%20I%27d%20probably%20break%20down%20and%20cry%0AWhoa%2C%20oh%2C%20oh%0ASweet%20child%20o%27%20mine%0AWhoa%2C%20oh%2C%20oh%2C%20oh%0ASweet%20love%20of%20mine%0AShe%27s%20got%20eyes%20of%20the%20bluest%20skies%0AAs%20if%20they%20thought%20of%20rain%0AI%27d%20hate%20to%20look%20into%20those%20eyes%20and%20see%20an%20ounce%20of%20pain%0AHer%20hair%20reminds%20me%20of%20a%20warm%20safe%20place%0AWhere%20as%20a%20child%20I%27d%20hide%0AAnd%20pray%20for%20the%20thunder%20and%20the%20rain%20to%20quietly%20pass%20me%20by%0AWhoa%2C%20oh%2C%20oh%0ASweet%20child%20o%27%20mine%0AWhoa%20whoa%2C%20oh%2C%20oh%2C%20oh%0ASweet%20love%20of%20mine%0AWhoa%2C%20yeah%0AWhoa%2C%20oh%2C%20oh%2C%20oh%0ASweet%20child%20o%27%20mine%0AWhoa%2C%20oh%2C%20whoa%2C%20oh%0ASweet%20love%20of%20mine%0AWhoa%2C%20oh%2C%20oh%2C%20oh%0ASweet%20child%20o%27%20mine%0AOoh%2C%20yeah%E2%80%A6&op=translate
		#
		# https://translate.google.com/?sl=auto&tl=iw&text=She%27s%20got%20a%20smile%20that%20it%20seems%20to%20me%3B%20Reminds%20me%20of%20childhood%20memories%0Where%20everything%20was%20as%20fresh%20as%20the%20bright%20blue%20sky%3B%20Now%20and%20then%20when%20I%20see%20her%20face%0She%20takes%20me%20away%20to%20that%20special%20place%3B%20And%20if%20I%20stare%20too%20long%2C%20I%27d%20probably%20break%20down%20and%20cry%0Whoa%2C%20oh%2C%20oh%3B%20Sweet%20child%20o%27%20mine%0Whoa%2C%20oh%2C%20oh%2C%20oh%3B%20Sweet%20love%20of%20mine%0She%27s%20got%20eyes%20of%20the%20bluest%20skies%3B%20As%20if%20they%20thought%20of%20rain%0I%27d%20hate%20to%20look%20into%20those%20eyes%20and%20see%20an%20ounce%20of%20pain%3B%20Her%20hair%20reminds%20me%20of%20a%20warm%20safe%20place%0Where%20as%20a%20child%20I%27d%20hide%3B%20And%20pray%20for%20the%20thunder%20and%20the%20rain%20to%20quietly%20pass%20me%20by%0Whoa%2C%20oh%2C%20oh%3B%20Sweet%20child%20o%27%20mine%0Whoa%20whoa%2C%20oh%2C%20oh%2C%20oh%3B%20Sweet%20love%20of%20mine%0Whoa%2C%20yeah%3B%20Whoa%2C%20oh%2C%20oh%2C%20oh%0Sweet%20child%20o%27%20mine%3B%20Whoa%2C%20oh%2C%20whoa%2C%20oh%0Sweet%20love%20of%20mine%3B%20Whoa%2C%20oh%2C%20oh%2C%20oh%0Sweet%20child%20o%27%20mine%3B%20Ooh%2C%20yeah%0Whoa%2C%20yeah%3B%20Whoa%2C%20oh%2C%20oh%2C%20oh%0Sweet%20child%20o%27%20mine%3B%20Whoa%2C%20oh%2C%20whoa%2C%20oh%0Sweet%20love%20of%20mine%3B%20Whoa%2C%20oh%2C%20oh%2C%20oh%0Sweet%20child%20o%27%20mine%3B%20Ooh%2C%20yeah%0Ooh%2C%20sweet%20love%20of%20mine%3B%20Where%20do%20we%20go?%0Where%20do%20we%20go%20now?%3B%20Where%20do%20we%20go?%0Ooh%2C%20oh%2C%20where%20do%20we%20go?%3B%20Where%20do%20we%20go%20now?%0Oh%2C%20where%20do%20we%20go%20now?%3B%20Where%20do%20we%20go?%20Sweet%20child%0Where%20do%20we%20go%20now?%3B%20Ay%2C%20ay%2C%20ay%2C%20ay%2C%20ay%2C%20ay%2C%20ay%2C%20ay%0Where%20do%20we%20go%20now?%3B%20Ah%2C%20ah%0Where%20do%20we%20go?%3B%20Oh%2C%20where%20do%20we%20go%20now?%0Oh%2C%20where%20do%20we%20go?%3B%20Oh%2C%20where%20do%20we%20go%20now?%0Where%20do%20we%20go?%3B%20Oh%2C%20where%20do%20we%20go%20now?%0Now%2C%20now%2C%20now%2C%20now%2C%20now%2C%20now%2C%20now%3B%20Sweet%20child%0Sweet%20child%20of%20mine%3B%20&op=translate

		# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
		# print(response)
		#
		# She%27s%20got%20a%20smile%20that%20it%20seems%20to%20me%3B%20Reminds%20me%20of%20childhood%20memories%0AWhere%20everything%20was%20as%20fresh%20as%20the%20bright%20blue%20sky%0ANow%20and%20then%20when%20I%20see%20her%20face%0AShe%20takes%20me%20away%20to%20that%20special%20place%0AAnd%20if%20I%20stare%20too%20long%2C%20I%27d%20probably%20break%20down%20and%20cry%0AWhoa%2C%20oh%2C%20oh%0ASweet%20child%20o%27%20mine%0AWhoa%2C%20oh%2C%20oh%2C%20oh%0ASweet%20love%20of%20mine%0AShe%27s%20got%20eyes%20of%20the%20bluest%20skies%0AAs%20if%20they%20thought%20of%20rain%0AI%27d%20hate%20to%20look%20into%20those%20eyes%20and%20see%20an%20ounce%20of%20pain%0AHer%20hair%20reminds%20me%20of%20a%20warm%20safe%20place%0AWhere%20as%20a%20child%20I%27d%20hide%0AAnd%20pray%20for%20the%20thunder%20and%20the%20rain%20to%20quietly%20pass%20me%20by%0AWhoa%2C%20oh%2C%20oh%0ASweet%20child%20o%27%20mine%0AWhoa%20whoa%2C%20oh%2C%20oh%2C%20oh%0ASweet%20love%20of%20mine%0AWhoa%2C%20yeah%0AWhoa%2C%20oh%2C%20oh%2C%20oh%0ASweet%20child%20o%27%20mine%0AWhoa%2C%20oh%2C%20whoa%2C%20oh%0ASweet%20love%20of%20mine%0AWhoa%2C%20oh%2C%20oh%2C%20oh%0ASweet%20child%20o%27%20mine%0AOoh%2C%20yeah%E2%80%A6

# return fullL

	# return f'Todo : {item}'
	# return translated
	# print("!!!!!")
	# return
	fullL = []
	# fullt = "<h1>"+item+"</h1>"

	while lyrics[0] is "":
		lyrics = lyrics[1:]
	while translated[0] is "" or translated[0].strip() == ".":
		translated = translated[1:]

	# finalLyrics = []
	# finalTranslated = []
	# for l in lyrics:
	# 	if l.strip() != ".":
	# 		finalLyrics.append(l)
	# for l in translated:
	# 	if l.strip() != ".":
	# 		finalTranslated.append(l)
	# lyrics = finalLyrics
	# translated = finalTranslated
	toff = 0
	for c in range(len(lyrics)):
		# fullL.append(lyrics[c]+"@")
		# fullL.append(lyrics[c])
		addL = lyrics[c]
		if addL.strip() == ".":
			addL = " "

		if debug:
			fullL.append("E: "+addL +"@@")
		else:
			fullL.append(addL)


		if c+toff < len(translated):
			addT = translated[c+toff]
			if addT.strip() == ".":
				addT = " "
			# fullL.append(translated[c])
			if addT.strip() == ".":
				fullL.append(f"-1 {c} {toff}, {addT}")
				toff+=1
				# addT = translated[c+toff]
				# if addT.strip() == ".":
				# 	addT = " "
			if debug:
				fullL.append("T: "+addT)
			else:
				fullL.append(addT)
		fullL.append("")
		fullL.append("")
		# fullt += "<pre>"+lyrics[c] + "</pre>"
		# fullt += "<pre>"+translated[c][::-1] + "</pre>"
		# print(lyrics[c])
		# print(translated[c])
		print("")

	print(" @ @ @ @ @ @  @")
	print(fullL)
	return fullL, song_info, item.replace(" ","⠀")

from flask import Flask, render_template, request, redirect  # add

# from Translate import Danilator
# Danilator.search("new soul")

key_var_name = '436cb96eb2d94be29c81bfd3dd5fcd5e'
# if not key_var_name in os.environ:
#     raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = '436cb96eb2d94be29c81bfd3dd5fcd5e'

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
app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template('base.html', full = None)

# loading = "aaaaaaaaa"
@app.route('/', methods=['POST'])
def my_form_post():
	query = request.form['text']
	if query is "":
		return  render_template('base.html',title = u"\U0001F49A", full = None)
	processed_text = process_text(query)
	print("!!!!!!xxx!!!",processed_text)

	return get_all(processed_text, query)

def process_text(query):
	print("QQQQQQQQQQQQQQQQ",query)
	if query is "":
		# print("XXXXXXXXXXX")
		return  render_template('base.html',title = u"\U0001F49A", full = None)
	urlChecks = ["http","youtu","spotify"]
	url = False
	for check in urlChecks:
		if check.lower() in query.lower():
			url = True

	print("START")
	processed_text = ""
	if url:
		print(query,"!!!!!!!!!!!!!!!!!!!")
		query = str(re.search("(?P<url>https?://[^\s]+)", query).group("url"))
		print(query,"!!!!!!!!!!!!!!!!!!!!")
		html = getHTML(query)

		try:
			if "spotify" in query:
				full = html.title.string
				full = full.split(', a song by ')
				full[1] = full[1].split(" ")[0].replace(","," ")
				title, artist = full
				title = str(re.sub(r" ?\([^)]+\)", "", title))
				artist = str(re.sub(r" ?\([^)]+\)", "", artist))
				processed_text = title +" "+artist
				print(processed_text)
			else:
				processed_text = "-".join(html.title.string.split("-")[:-1]).replace("/"," ")
		except Exception as e:
			print("EEEEEEEEEEEEEEEEEE: Processing Text ",e)
			processed_text = ""
			return render_template('base.html', full = None)
		print("UUUUUUUUUUUUUUUUUUUUUU",processed_text)
		print("UUUUUUUUUUUUUUUUUUUUUU",processed_text)
		print("UUUUUUUUUUUUUUUUUUUUUU",processed_text)

	else:
		processed_text = query.upper()
	if processed_text == "":
		return " "
	return processed_text

def get_all(processed_text, text):
	a, song_info, title = doit(processed_text)
	# print(a)
	# return redirect('/lyrics/'+text)
	song_txt = ""
	if text is "/":
		text = ""

	if song_info is None or len(song_info) < 1:
		song_info.append(processed_text)
		song_info.append("___")


	if song_info[0] is not "":
		song_txt = song_info[0]
		for s in song_info[1:]:
			song_txt += " - "+s
		print("!!!!!!!!!!!!!!!!!!",song_info[0]+" - "+song_info[1])
		return render_template('base.html',tasks = a , title = song_txt, full = text.replace(" ","_"))
	return render_template('base.html', full = text.replace(" ","_"))
	# 	return render_template('base.html',tasks = a , title = song_txt, full = text.replace(" ","⠀"))
	# return render_template('base.html', full = text.replace(" ","⠀"))
	return a

#
# @app.route('/lyrics/<string:title>')
# def get_stairway(title):
# 	processed_text = process_text(title.replace("+"," "))
# 	print("!!!!!!!!!",processed_text)
# 	return get_all(processed_text)
#

@app.route('/<path:text>', methods=['GET', 'POST'])
def all_routes(text):
	print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
	text = text.replace("⠀"," ")
	if text is "/":
		text = ""
	print("@@@@@@@@@")
	print(text)
	if "lyrics/" in text:
		text = text.replace("lyrics/","")
	processed_text = process_text(text.replace("+"," "))
	print("!!!!!!!!!",processed_text)
	return get_all(processed_text, text)
	#
	# if text in refs:
	# 	return redirect(refs[text])
	# else:
	# 	return redirect("/")


if __name__ == "__main__":
   app.run(debug=True)

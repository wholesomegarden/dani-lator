# -*- coding: utf-8 -*-

# This simple app uses the '/translate' resource to translate text from
# one language to another.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

# import lyricwikia


#gen.py



# class gen:
# GENIUS_API_TOKEN = client_access_token = 'q2iKacoJeJRs5q6UC1AnYWN4IriZnwgV4FhoXWxIERxORuOb9GxUdAbWDD_K1D5q'


# item = input('Enter the song to find its lyrics: ')


import os, requests, uuid, json, re
import requests
from youtube_title_parse import get_artist_title
from google_trans_new import google_translator
from bs4 import BeautifulSoup, UnicodeDammit, NavigableString
translator = google_translator()

# from googletrans import Translator


# translator = Translator()
# import datetime

# GCS_API_KEY = 'AIzaSyCHOkya9h3n7BWA10S_CQQkz-p9Wlreh44'
# GCS_ENGINE_ID = 'Danilator'
# from lyrics_extractor import SongLyrics

def getHTML(url):
	headers_Get = {
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language': 'en-US,en;q=0.5',
			'Accept-Encoding': 'gzip, deflate',
			'DNT': '1',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests': '1'
		}
	searchPage = requests.get(url, headers=headers_Get)
	html = BeautifulSoup(searchPage.text,'html.parser')
	return html

def getLyrics(title):
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
		for paper in html.findAll("div",class_="SPZz6b"):
			for desc in paper.descendants:
				print("DDDDDDDD",desc)
			info = [desc.strip() for desc in paper.descendants if type(desc) == NavigableString]
			for i in info:
				song_info.append(i)
	lyrics=html.find_all("span", jsname="YS01Ge")
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
	n = 0
	parts = []
	print(lyricsText)
	print(type(lyricsText), len(lyricsText),len(lyricsText.split("\n")))
	maxChunks = 50
	for chunk in chunks(lyricsText.split("\n"), maxChunks):
		chunkT = "\n".join(chunk)
		print("!!!!!!!!!!!!","\n",chunkT)
		res = translator.translate(str(chunkT),lang_tgt="he")
		print("$$$$$$$$$$$$$$$$$$$$$")
		print(res)
		parts.append(res+"\n")
	# time.sleep(1)
		# n+=1
	# res = translator.translate(lyricsText,lang_tgt="he")
	print("########################@@@")
	print(parts)
	# translated = res.__dict__()["text"]
	translated = ("".join(parts)).split("\n")
	print("############################")
	print(translated)
	print("XXXXXXXXXXXXXXXXXXXXXXXXXXX")
	fullL = []
	# fullt = "<h1>"+item+"</h1>"
	for c in range(len(lyrics)):
		fullL.append(lyrics[c])
		if c < len(translated):
			fullL.append(translated[c])
		fullL.append("")
		fullL.append("")
		# fullt += "<pre>"+lyrics[c] + "</pre>"
		# fullt += "<pre>"+translated[c][::-1] + "</pre>"
		# print(lyrics[c])
		# print(translated[c])
		print("")
	print(" @ @ @ @ @ @  @")
	print(fullL)
	return fullL, song_info



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
	return render_template('base.html')

# loading = "aaaaaaaaa"
@app.route('/', methods=['POST'])
def my_form_post():
	query = request.form['text']
	processed_text = process_text(query)
	print("!!!!!!!!!",processed_text)
	return get_all(processed_text)

def process_text(query):
	print("QQQQQQQQQQQQQQQQ",query)
	if query is "":
		return  render_template('base.html',title = u"\U0001F49A")
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
			return render_template('base.html')
		print("UUUUUUUUUUUUUUUUUUUUUU",processed_text)
		print("UUUUUUUUUUUUUUUUUUUUUU",processed_text)
		print("UUUUUUUUUUUUUUUUUUUUUU",processed_text)
	else:
		processed_text = query
	if processed_text == "":
		return " "
	return processed_text

def get_all(processed_text):
	a, song_info = doit(processed_text)
	# print(a)
	# return redirect('/lyrics/'+text)
	song_txt = ""

	if song_info is None or len(song_info) < 1:
		song_info.append(processed_text)
		song_info.append("___")


	if song_info[0] is not "":
		song_txt = song_info[0]
		for s in song_info[1:]:
			song_txt += " - "+s
		print("!!!!!!!!!!!!!!!!!!",song_info[0]+" - "+song_info[1])
		return render_template('base.html',tasks = a , title = song_txt)
	return render_template('base.html')
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
	print("@@@@@@@@@")
	print(text)
	if "lyrics/" in text:
		text = text.replace("lyrics/","")
		processed_text = process_text(text.replace("+"," "))
		print("!!!!!!!!!",processed_text)
		return get_all(processed_text)
	#
	# if text in refs:
	# 	return redirect(refs[text])
	# else:
	# 	return redirect("/")


if __name__ == "__main__":
   app.run(debug=True)

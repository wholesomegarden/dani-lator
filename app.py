# -*- coding: utf-8 -*-

# This simple app uses the '/translate' resource to translate text from
# one language to another.

# This sample runs on Python 2.7.x and Python 3.x.
# You may need to install requests and uuid.
# Run: pip install requests uuid

import os, requests, uuid, json
# import lyricwikia


#gen.py


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

def doit(item):
	if item == "":
		return "", ["",""]
		# item = input('Enter the song to find its lyricsxx: ')
	lyricsText, song_info = getLyrics(item)
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
	fullL = []

	i = 0
	for r in response[0]['translations'][0]['text'][::-1].split("\n")[::-1]:
		# print(r)

		# fullL = [lyrics[i]+"\n"+r[::-1]]
		translated.append(r)
		i+=1

# return fullL

	# return f'Todo : {item}'
	# return translated
	# print("!!!!!")
	# return
	# fullL = []
	fullt = "<h1>"+item+"</h1>"
	for c in range(len(translated)):
		fullL.append(lyrics[c])
		fullL.append(translated[c][::-1])
		fullt += "<pre>"+lyrics[c] + "</pre>"
		fullt += "<pre>"+translated[c][::-1] + "</pre>"
		# print(lyrics[c])
		# print(translated[c])
		print("")
	return fullL, song_info

from flask import Flask, render_template, request, redirect  # add

# from Translate import Danilator
# Danilator.search("new soul")

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
app = Flask(__name__)

@app.route('/')
def my_form():
	return render_template('base.html')

# loading = "aaaaaaaaa"

@app.route('/', methods=['POST'])
def my_form_post():
	query = request.form['text']
	if query is "":
		return  render_template('base.html',title = u"\U0001F49A")
	urlChecks = ["http","youtu"]
	url = False
	for check in urlChecks:
		if check.lower() in query.lower():
			url = True

	print("START")
	proccessed_text = ""
	if url:
		html = getHTML(query)
		try:
			processed_text = "-".join(html.title.string.split("-")[:-1])
		except:
			processed_text = ""
			return render_template('base.html')
		print("UUUUUUUUUUUUUUUUUUUUUU",processed_text)
		print("UUUUUUUUUUUUUUUUUUUUUU",processed_text)
		print("UUUUUUUUUUUUUUUUUUUUUU",processed_text)

	else:
		processed_text = query.upper()
	print("!!!!!!!!!",processed_text)
	a, song_info = doit(processed_text)
	# print(a)
	# return redirect('/lyrics/'+text)
	if song_info[0] is not "":
		print("!!!!!!!!!!!!!!!!!!",song_info[0]+" - "+song_info[1])
		return render_template('base.html',tasks = a , title = song_info[0]+" - "+song_info[1])
	return render_template('base.html')
	return a


@app.route('/lyrics/<string:title>')
def get_stairway(title):
	# text = request.form['text']
	# processed_text = text.upper()
	# print("!!!!!!!!!",processed_text)
	# a = doit(processed_text)
	# print(a)
	print("!!!!!!!!!!!!")
	return doit(title)
	# return a


if __name__ == "__main__":
   app.run(debug=True)


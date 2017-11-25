#!/usr/bin/env python3
# by aribeiro

import requests
import urllib.request
from bs4 import BeautifulSoup
import sys

array = []

def check_readme(url):
	req = requests.get(url)
	soup = BeautifulSoup(req.text, "lxml")
	for link in soup.find_all('a'):
		if link.get('href') == "README" :
			f = urllib.request.urlopen(url + '/' + link.get('href'))
			myfile = f.read()
			if myfile in array:
				myfile = ""
			else:
				array.append(myfile)
				print(myfile)
			break
		elif link.get('href') != "../":
			check_readme(url + '/' + link.get('href'))

def main(arg):
	url = 'http://' + arg + '/.hidden/'
	check_readme(url)


if __name__ == "__main__":
	try:
		arg = sys.argv[1]
		main(arg)
	except IndexError:
		print("error arg")

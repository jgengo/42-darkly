#!/usr/bin/env python3
# by aribeiro

import requests
import urllib.request
from bs4 import BeautifulSoup
import sys

the_list = []

def check_readme(url):
	req = requests.get(url)
	soup = BeautifulSoup(req.text, "lxml")
	for link in soup.find_all('a'):
		if link.get('href') == "README" :
			f = urllib.request.urlopen(url + '/' + link.get('href'))
			myfile = f.read()
			if myfile not in the_list:
				the_list.append(myfile)
				print(myfile)
			break
		elif link.get('href') != "../":
			check_readme(url + '/' + link.get('href'))

def main(arg):
	url = 'http://' + arg + '/.hidden/'
	check_readme(url)
	with open('result_crawler.txt', 'w') as file_handler:
		for item in the_list:
			file_handler.write("{}\n".format(item))

if __name__ == "__main__":
	try:
		arg = sys.argv[1]
		main(arg)
	except IndexError:
		print("=> Error: one argument is missing (ex: python3 script.py 192.168.1.59)")
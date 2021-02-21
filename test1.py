''' 
*Requirements
1. requests
2. BeautifulSoup4
2. os

To install requests library write pip install requests in terminal or command.
To install BeautifulSoup4 library write pip install BeautifulSoup4 in terminal or command.
OS is built in library in python so need to install.

'''


import requests
from bs4 import BeautifulSoup
import os 

f = open("links.txt", "r")
links = f.readlines()

for i in range(0,28):  # Here you have to input how many link in your test file
	
	url = links[i]

	header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0",
			  	"Accept": "*/*",
				"Accept-Language": "en-US,en;q=0.5",
				"Accept-Encoding": "gzip, deflate, br",
				"Origin": "null",
				"Connection": "keep-alive"
	}


	request = requests.get(url, header)
	soup = BeautifulSoup(request.text, 'lxml')
	response_code = request.status_code
	x = requests.head(url)


	if response_code == 406:
		pass

	else:

		#Create a new file named "newlinks.txt" then you should run this script
		
		f = open("newlinks.txt", "a") 
		f.write(f"Response code: {response_code} \nUrl: {url} Head Request: {x.headers}\n\n")
		f.close()
		
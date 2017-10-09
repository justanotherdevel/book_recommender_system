import requests
from lxml import html
import urllib
from bs4 import BeautifulSoup
import re
import time 
import webc as w
import json

def step_uno(url="https://www.amazon.in/Books/b?ie=UTF8&node=976389031"):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	response=requests.get(url,headers=headers)
	html=response.text
	time.sleep(1)
	soup=BeautifulSoup(html,'lxml')
	genre=soup.find('div',class_="acs-en-row")
	genre_list=genre.find_all('p')
	glist=[i.text for i in genre_list]
	#############################################################################
	genre_dict={}
	genre_links=genre.find_all('a')
	glinks=[i.get('href') for i in genre_links]
	for i in range(len(glinks)):
		genre_dict[glist[i]]=glinks[i]
	for j in range(len(glist)):
		print(j+1,'.',glist[j])
	g=int(input("Enter index of choice:"))
	rlink=genre_dict[glist[g-1]]	
        with open("urlList.json", 'w') as f:
                json.dump(genre_dict, f, indent=4)  
	req_link=urllib.parse.urljoin('https://www.amazon.in',rlink)
	return str(req_link)	
	
if __name__=="__main__":
	step_uno()

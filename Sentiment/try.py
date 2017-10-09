import requests
import lxml
from bs4 import BeautifulSoup
import re
import time 
import allgenre as ag
import webc as wc
import json

def web():
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	url=ag.step_uno()
	response=requests.get(url,headers=headers)
	html=response.text
	time.sleep(3)
	soup=BeautifulSoup(html,'html.parser')
	books=soup.find_all('h2',class_="a-size-medium s-inline  s-access-title  a-text-normal")
	# for i in books:
	# 	print(i.text)
	book_link=soup.find_all('a',class_='a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal')
	# for i in book_link:
	# 	print(i.get('href'))
	f=open("comments.json","w")
	ac_dict={}
	for i in range(len(book_link)):
		j=book_link[i].get('href')
		clist=wc.web(j)
		ac_dict[books[i].text]=(clist)
	json.dump(ac_dict,f)
	f.close()


if __name__=="__main__":
	web()	
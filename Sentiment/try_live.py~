import requests
import lxml
from bs4 import BeautifulSoup
import re
import time 
import allgenre as ag
import webc as wc
import json
import rate_live
import sys

def web(g):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    genre_dict = dict()
    with open("/home/shashwat/Programs/Python/book_recommender_system/Sentiment/urlList.json", 'r') as f:
        genre_dict = json.load(f)
    
    with open("/home/shashwat/Programs/Python/book_recommender_system/Sentiment/glist.json",'r') as f:
        glist = json.load(f)
    rlink = genre_dict[glist[g-1]]
    url = urllib.parse.urljoin('https://www.amazon.in', rlink)
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
    ac_dict={}
    for i in range(len(book_link)):
        j=book_link[i].get('href')
        clist=wc.web(j)
        ac_dict[books[i].text]=(clist)
    with open("/home/shashwat/Programs/Python/book_recommender_system/Sentiment/comments.json", 'w') as f:	
        json.dump(ac_dict,f)
    rate_live.nProcess()


if __name__=="__main__":
    g = int(sys.argv[1])
    web(g)	

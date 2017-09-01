import requests
from bs4 import BeautifulSoup
import re
import time 

def web(url):
	response=requests.get(url)
	html=response.text
	time.sleep(5)
	soup=BeautifulSoup(html,'html.parser')
	# print(html)
	try:
		avg=soup.find('div',id="avgRating")
		print(avg.text[6:9])
		cmnt=soup.find_all('div',id=re.compile('revData-dpReviewsMostHelpfulAUI-'))
		[s.extract() for s in soup.find_all("script")]
		[s.extract() for s in soup.find_all("span")]
		# 		cmnts=[]
		for i in cmnt:
			print(i.text)	
			# cmnts.append(i.text)
	except:
		print("HEAVY TRAFFIC")
	


if __name__=="__main__":
	url=input("Enter URL:")
	web(url)	
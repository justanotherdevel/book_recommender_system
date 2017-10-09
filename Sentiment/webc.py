import requests
import lxml
from bs4 import BeautifulSoup
import re
import time 

def web(url):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	response=requests.get(url,headers=headers)
	html=response.text
	time.sleep(3)
	soup=BeautifulSoup(html,'lxml')
	# print(html)
	try:
		# avg=soup.find('div',id="reviewSummary")
		# print(avg.text[:3])
		# cmnt=soup.find_all('div',id=re.compile('customer_review-'))
		cmnt=soup.find_all('div',class_='a-expander-content a-expander-partial-collapse-content')
		[s.extract() for s in soup.find_all("script")]
		[s.extract() for s in soup.find_all("span")]
		cmnts=[]
		for i in cmnt:
			# print(i.text) 
			cmnts.append(i.text)
		# print(cmnts)
		return cmnts
		
	except:
		return "HEAVY TRAFFIC"
	


if __name__=="__main__":
	url=input("Enter URL:")
	web(url)

	
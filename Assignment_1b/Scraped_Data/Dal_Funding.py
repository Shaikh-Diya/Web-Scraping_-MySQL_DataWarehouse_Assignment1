from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

dal_funding_url = 'https://www.dal.ca/faculty/gradstudies/funding/studentsinprogram/bursariesawardstravel.html'
#opening up connection and grabbing the pages
uClient = uReq(dal_funding_url)
page_html = uClient.read()
uClient.close()
#html parser
page_soup = soup(page_html, "html.parser")
funding_container = page_soup.findAll("div", attrs={"class":"text parbase section"})
#num_rNews = print(len(rNews_container))


for x in funding_container[1:]:
	fundingTitle = x.findAll('tr').text
	#for y in fundingTitle:
	#	print(y.text)

#xml Insertion needed manually
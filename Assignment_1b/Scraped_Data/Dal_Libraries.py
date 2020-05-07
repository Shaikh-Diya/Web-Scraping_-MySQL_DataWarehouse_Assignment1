from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

dal_funding_url = ''
#opening up connection and grabbing the pages
uClient = uReq(dal_library_url)
page_html = uClient.read()
uClient.close()
#html parser
page_soup = soup(page_html, "html.parser")
library_container = page_soup.findAll("div", attrs={"class":"text parbase section"})
#num_rNews = print(len(rNews_container))

for x in library_container[1:]:
	library_loc = x.findAll('').text
	#for y in LocationTitle:
	#	print(y.text)

#xml Insertion needed manually
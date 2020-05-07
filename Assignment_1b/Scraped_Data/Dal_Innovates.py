from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

dal_innovates_url = 'https://dalinnovates.ca/'
#opening up connection and grabbing the pages
uClient = uReq(dal_innovates_url)
page_html = uClient.read()
uClient.close()
#html parser
page_soup = soup(page_html, "html.parser")
dalInnovates_container = page_soup.findAll("div", attrs={"class":"sidebar-nav__pane--nav current"})
#num_dalInnovates = print(len(dalInnovates_container))
#d_innovates = dalInnovates_container[1]


for dalInnovates in dalInnovates_container[1:]:
	programs = dalInnovates.findAll('li')
	for programName in programs:
		print(programName.text)
#xml Insertion needed manually

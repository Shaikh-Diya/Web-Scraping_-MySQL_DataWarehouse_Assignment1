from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

dal_rNews_url = 'https://www.dal.ca/research/ResearchIntheNews.html'
#opening up connection and grabbing the pages
uClient = uReq(dal_rNews_url)
page_html = uClient.read()
uClient.close()
#html parser
page_soup = soup(page_html, "html.parser")
rNews_container = page_soup.findAll('li')
# print(rNews_container)

f = open("Dal_News.xml", "w+", encoding = 'utf-8')
f.write("<table name = \"Dal_News\">")
i = 0
for news in rNews_container[48:]:
	i = i+1
	f.write("<record><column name=\"NewsId\">" + str(i) + "</column>")
	f.write("<column name=\"NewsName\">" + news.text.replace('&', '') + "</column></record>")

f.write("</table>") 
	

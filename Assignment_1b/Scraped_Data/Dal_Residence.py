from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

dal_residence_url = 'https://www.dal.ca/campus_life/residence_housing/residence/halifax-campus/res-buildings-halifax.html'
#opening up connection and grabbing the pages
uClient = uReq(dal_residence_url)
page_html = uClient.read()
uClient.close()
#html parser
page_soup = soup(page_html, "html.parser")
residence_container = page_soup.findAll("div",attrs="text parbase section")
#residence_halls = residence_container[1]

f = open("Dal_Residence.xml", "w+", encoding = 'utf-8')
f.write("<table name = \"Dal_Residence\">")
i = 0

for buildings in residence_container[1:]:
    Residences = buildings.findAll('li')
    for residenceName in Residences:
    	i = i+1
    	f.write("<record><column name=\"ResidenceId\">" + str(i) + "</column>")
    	f.write("<column name=\"ResidenceName\">" + residenceName.text.replace('&', '') + "</column></record>")


f.write("</table>") 


# for x in residence_halls.findAll('ul'):
#     ResidenceName = x.text
#     print(ResidenceName)
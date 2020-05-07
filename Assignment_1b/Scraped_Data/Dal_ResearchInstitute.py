from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

dal_InstituteCentres_url = 'https://www.dal.ca/research/centres_and_institutes.html'
#opening up connection and grabbing the pages
uClient = uReq(dal_InstituteCentres_url)
page_html = uClient.read()
uClient.close()
#html parser
page_soup = soup(page_html, "html.parser")
InstituteCentre_container = page_soup.findAll("div", attrs={"class":"text parbase section"})
#num_iCenters = print(len(instituteCenter_container))
#icentres = instituteCenter_container[1]


f = open("Dal_ResearchInstitute.xml", "w+", encoding = 'utf-8')
# .write("<?xml version= "1.0" endcoding = \"utf-8\"?>")
f.write("<table name = \"Dal_Institute_Centre\">")
i = 0

for centres in InstituteCentre_container[1:]:
	InstituteCentreName = centres.findAll('li')
	for centreNames in InstituteCentreName:
		i = i+1
		f.write("<record><column name=\"InstituteCentreId\">" + str(i) + "</column>")
		f.write("<column name=\"InstituteCentreName\">" + centreNames.text.replace('&', '') + "</column></record>")
		#print(centerNames.text)
f.write("</table>") 


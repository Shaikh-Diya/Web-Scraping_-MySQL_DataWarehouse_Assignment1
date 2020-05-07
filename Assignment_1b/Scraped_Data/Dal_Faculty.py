
from xml.dom import minidom
import os

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

dal_faculties_url = 'https://www.dal.ca/academics/faculties.html'
#opening up connection and grabbing the page
uClient = uReq(dal_faculties_url )
page_html = uClient.read()
uClient.close()
#html parser
page_soup = soup(page_html, "html.parser")
faculties_container = page_soup.findAll("div", attrs={"class":"text parbase section"})
num_faculties = print(len(faculties_container))



f = open("Dal_Faculty.xml", "w+", encoding = 'utf-8')
i = 0
f.write("<table name = \"Dal_Faculty\"> ")
for x in faculties_container[1:]:
	facultyName = x.find('a').text
	i = i+1
	f.write("<record><column name=\"facultyId\">" + str(i) + "</column>")
	f.write("<column name=\"facultyName\">" + facultyName.replace('&', '') + "</column></record>" )
	
f.write("</table>") 
	




#creating xml file and insertion of data
#root = minidom.Document()
#xml = root.createElement('Faculty')
#root.appendChild(xml)
#productChild = root.createElement('facultyId')
#xml.appendChild(productChild)

#childOfProduct = root.createElement('facultyName')
#childOfProduct.appendChild(root.createTextNode(''))
#productChild.appendChild(childOfProduct)

#xml_str = root.toprettyxml(indent="\t")
#sava_path_file = "faculty.xml"
#with open(sava_path_file,"w") as f:
#		f.write(xml_str)
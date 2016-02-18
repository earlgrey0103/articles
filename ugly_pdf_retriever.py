import requests
import time
import os

from bs4 import BeautifulSoup


try:
    os.mkdir("pdfs")
except:
    pass

response = requests.get("http://www.dni.gov/index.php/resources/bin-laden-bookshelf?start=1")

if response.status_code == 200:
    
    html = BeautifulSoup(response.content)


link_list = []

for i in html.findAll("a")[54:]:
    if "pdf" in i['href'] and "Arabic" not in i.text:
        link_list.append("http://www.odni.gov%s" % i['href'])
        
for i in link_list:
    response = requests.get(i)
    file_name = i.split("/")[::-1][0]
    fd = open("pdfs/%s" % file_name,"wb")
    fd.write(response.content)
    fd.close()
    
    time.sleep(1)
        

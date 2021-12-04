from bs4 import BeautifulSoup
import requests
from io import StringIO
import lxml
import csv 
import time

input = open('MasaPost.csv', newline='')
output = open('MasaNew2.csv', 'w', newline='',encoding='utf-8')
csvreader = csv.reader(input, delimiter=' ', quotechar='|')
csvwriter = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow(['Title', 'Text', 'Images Src'])
i=0
for row in csvreader:
    page = requests.get(row[0], headers={'User-Agent': 'Mozilla/5.0'})
    time.sleep(0.5)
    html = page.content.decode("utf-8")
    soup = BeautifulSoup(StringIO(html), "lxml")
    title = soup.title.text # Blog title
    body = soup.find("div", {"class": "col-12"})
    try:
        blog = soup.find("div", {"class": "col-12"}).find("div", {"class": "col-12"}).findAll("p") ##.text # Blog Content
    except Exception:
        print("body Cannot find")
        continue
    imageSrc = None
    try:
        image = body.find('img')# Image source
    except Exception:
        print("img Cannot find")
        pass
    if image is not None:
        imageSrc =(image['src'])
    csvwriter.writerow([title, blog, imageSrc])
    print (i)
    i = i+1
output.close()
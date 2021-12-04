from bs4 import BeautifulSoup
import requests
from io import StringIO
import lxml
import csv 
import time
from urllib3.exceptions import InsecureRequestWarning

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

input = open('final.csv', newline='')
output = open('MasaData2.csv', 'w', newline='',encoding='utf-8')
csvreader = csv.reader(input, delimiter=' ', quotechar='|')
csvwriter = csv.writer(output, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
csvwriter.writerow(['Title', 'Text'])
i=0

for row in csvreader:
    try:
        page = requests.get(row[0], verify=False,headers={'User-Agent': 'Mozilla/5.0'})
        time.sleep(0.5)
        html = page.content.decode("utf-8")
        soup = BeautifulSoup(StringIO(html), "lxml")

        try:
            title = soup.find("h2").text # Blog title
        except Exception:
            print("No Title Found")
        try:
            results = soup.find("div", {"class": "no-overflow"})
        except Exception:
            print("Body Cannot find")
   
    except Exception:
        title = ' - '
        results = ' - '
        print("Row Cannot find")
        
    csvwriter.writerow([title,results])
    print (i)
    i = i+1
output.close()

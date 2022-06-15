import requests
import os
from bs4 import BeautifulSoup

url = "https://urlhaus.abuse.ch/downloads/text_recent/"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

drl = str(os.getcwd())
arr = soup.body.get_text()  


k = arr.split('\n')
f = open(drl+"/mozi.txt", "w") 

count = 0  

for i in range(0, 80): 
    
    if(k[i].find("zi.") != -1):
        f.write(k[i])
        count = count + 1

print("count: ", count)
f.close


f = open("mozi.txt", 'r')


f.close



# -*- coding: utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup
from urllib import request
import hashlib

drl = str(os.getcwd())
print(drl)
path = './mozi_down' 
try: 
    if not os.path.exists(path): 
        os.makedirs(path) 
except OSError: print("Error: Cannot create the directory {}".format(path))

print("===========start==========")
print("<  Mozi.txt file exist?  >")
print("  Yes: 1     No : 2  ")
a = input()
if a != '1':
    f = open(drl+"/mozi.txt", "w")
    f.write("\n")
    f.close
    print("==== mozi.txt created ===")
print("============================")
print("<  mozi.txt in upload dowonload URL?  >")
print("   <  if you have one, press = 1  > ")

user_start = input()

if a == '1':
    f = open(drl+"/mozi.txt", 'r')
    k = 0
    arr = []

    
    while True:
        line = f.readline()
        if not line: break
        arr.append(line[:-1])
    f.close()

    f = open(drl + "/search_MD5.txt", "w") 
    for i in arr:

        if i == "":
            break
        ipaddr = str(i).split('/')[2]
        ipaddr = ipaddr.split(':')[0]
        print(ipaddr)
        path2 = path + '/' + str(ipaddr)
        try:   
            if not os.path.exists(path2): 
                os.makedirs(path2) 
        except OSError: print("Error: Cannot create the directory {}".format(path2))

        file_name = i.split('/')[-1].split('.')
        del file_name[1]
        file_name.insert(1, '.zip')
        file_name_end = str("".join(file_name))
        

        try:
            response = requests.get(i)
        except requests.exceptions.Timeout as errd:
            print("Timeout Error : ", errd)
            print("=====================================================")
            continue
            
        
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting : ", errc)
            print("=====================================================")
            continue
            
        except requests.exceptions.HTTPError as errb:
            print("Http Error : ", errb)
            print("=====================================================")
            continue
            
        # Any Error except upper exception
        except requests.exceptions.RequestException as erra:
            print("AnyException : ", erra)
            print("=====================================================")
            continue
            
        
        file = open(path2 + '/' + file_name_end, "wb")
        file.write(response.content)
        file.close

        file = open(path2 + '/' + file_name_end, "rb")
        data  = file.read()
        file.close
    
            
        f.write(" MD5: " + hashlib.md5(data).hexdigest().swapcase() +" URL: "+ i+ "\n")
        print(" MD5:" + hashlib.md5(data).hexdigest().swapcase()+ "URL:" + i )
        print("=====================================================")
    f.close 
    print("------------search_MD5_fin.txt created------------")

    f = open(drl + "/search_MD5.txt", 'r')
    md_data = []
    while True:
        line = f.readline()
        if not line:break
        md_data.append(line[:-1].split(" "))

    md_data.sort(key=lambda md_data:md_data[1])
    f.close

    f = open(drl + "/search_MD5_fin.txt", 'w')
    for i in md_data:
        f.write(str(i)+"\n")
    f.close

import os
import re
#Acess File by given address file path
file=open("D:/SOFTWARE ALL/python3.6/Programs/my_file.txt")
#reading file line by line
f_url=[]
for line in file.readlines():
    urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
    #if no any link in line then pass otherwise add an list
    if len(urls)==0:
        pass
    else:
        f_url.append(urls)
#output 
l=len(f_url)
print("Occurrence Found:"+str(l) +" " +"First Occurrence:"+ "".join(f_url[0]))
        
    

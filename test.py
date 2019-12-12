import os
#import sys
import hashlib
#import importlib
import uuid

path="e:\\books"
dirs = []
files= []
items = os.listdir(path)
for item in items:
    item = os.path.join(path, item)
    if os.path.isdir(item):
        print(item)
        dirs.append(item)
    if os.path.isfile(item):
        #print(item, os.path.getsize(item))
        with open(item,'rb') as d:
            fcontent = d.read()
            fhash = hashlib.md5()
            fhash.update(fcontent)
            (folder,tempfname) = os.path.split(item)
            print(tempfname)
            (filename,extension) = os.path.splitext(tempfname)
            print(filename, extension)
            print(d.name,fhash.hexdigest())

#importlib.reload(sys)

print(uuid.uuid1())

with open("D:\\text.txt", 'a') as f:
   f.write("\nHello Python!")

# with open("D:\\t.pdf",'rb') as pdf:
#     content=pdf.read()
#     hash1 = hashlib.md5()
#     hash1.update(content) 
#     print(hash1.hexdigest())
#     print(pdf.name)
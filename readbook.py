import os
import hashlib
import uuid
import datetime

#write data to text
def writeToTest(path,text):
    with open(path,'a') as f:
        f.write(text) 

# format sql command
def formatSql(name,path,md5):
    bookid = uuid.uuid1()
    return "\nINSERT INTO `BOOKS`(`BookId`, `BookName`, `BookPath`, `Md5`, `CreateDate`) VALUES ('%s','%s','%s','%s',CURRENT_TIMESTAMP());" %(bookid,name,path,md5)

# find all files in a folder and subfolder
def findFiles(path, files):
    if files is None:
        files = []
    items = os.listdir(path)
    for item in items:
        item = os.path.join(path, item)
        if os.path.isfile(item):
            files.append(item)
        if os.path.isdir(item):
           findFiles(item, files)
    
    return files

# compute md5 and return all the file info with md5
def computeMd5(file):
    result = []
    result.append(file.replace('\\','\/').replace("\'","\\'"))  
    with open(file,'rb') as fc:
        fcontent = fc.read()
        fhash = hashlib.md5()
        fhash.update(fcontent)
        (fpath,tempfname) = os.path.split(file)
        #(filename,extension) = os.path.splitext(tempfname)       
        result.append(tempfname.replace("\'","\\'"))
        md5 = fhash.hexdigest()
        result.append(md5)
        result.append(fpath)
    
    return result

if __name__=='__main__':
    print(datetime.datetime.now())
    fileitems = findFiles("F:\\books",[])
    print(datetime.datetime.now())
    sqlcontent = "use books;"
    sqlpath = "d:\\sql.txt"
    for fi in fileitems:
        tpfn = os.path.split(fi)[1]
        if not tpfn.startswith('.'):
            re = computeMd5(fi)
            sqlcontent += formatSql(re[1],re[0],re[2])
        #print(fi)
    print(datetime.datetime.now())
    #write to the file
    writeToTest(sqlpath, sqlcontent)

import os
import hashlib
import uuid
import datetime
import pymysql

sqlbase = "INSERT INTO `BOOKS`(`BookId`, `BookName`, `BookPath`, `Md5`) VALUES (%s,%s,%s,%s)"

def writeToDb(sql,paras):
    try:
        conn = pymysql.connect("localhost","root","173170329","books")
        cursor = conn.cursor()
        cursor.executemany(sql,paras)
        conn.commit()
        conn.close()
    except:
        print("Error promed")   

#write data to text
def writeToTest(path,text):
    with open(path,'a') as f:
        f.write(text) 

# format sql command
def formatSql(name,path,md5):
    bookid = uuid.uuid1()
    return "INSERT INTO `BOOKS`(`BookId`, `BookName`, `BookPath`, `Md5`, `CreateDate`) VALUES ('%s','%s','%s','%s',CURRENT_TIMESTAMP());" %(bookid,name,path,md5)

# format the paras in multi execute sql
def formatListItem(name,path,md5):
    id = uuid.uuid1()
    return "('%s','%s','%s','%s')" %(id,name,path,md5)

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

def formatPar(paras):
    data = "("
    for para in paras:
        data+=para
    
    print(data)
    return data +")"

if __name__=='__main__':
    print(datetime.datetime.now())
    fileitems = findFiles("E:\\test",[])
    print(datetime.datetime.now())    
    sqlcontent = ""
    sqlpath = "d:\\sql.txt"
    exesql = ""
    sqlparas= "("
    for fi in fileitems:
        tpfn = os.path.split(fi)[1]
        if not tpfn.startswith('.'):
            re = computeMd5(fi)
            text = formatSql(re[1],re[0],re[2])
            #writeToDb(text)
            sqlcontent+= "\n" + text
            exesql += text
            if sqlparas is "(":
                sqlparas+= formatListItem(re[1],re[0],re[2])
            else:
                sqlparas += (","+formatListItem(re[1],re[0],re[2]))
        #print(fi)
    sqlparas +=")"
    print(datetime.datetime.now())
    print(sqlparas)
    # writeToTest("d:\\par.txt",sqlparas    
    writeToDb(sqlbase,sqlparas)
    #write to the file
    writeToTest(sqlpath, sqlcontent)
    writeToTest("d:\\t.txt",exesql)
 

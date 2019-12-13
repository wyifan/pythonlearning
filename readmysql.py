import pymysql

db = pymysql.connect("localhost","root","123456","books")

cursor = db.cursor()

sql = "select * from books where bookid='f72d1ef0-1b24-11ea-bb88-70c94ee665be'"
sqlbase = "INSERT INTO `books`(`BookId`, `BookName`, `BookPath`, `Md5`) VALUES (%s,%s,%s,%s)"
data =[('c2906c1c-1da7-11ea-adb9-72c94ee665bd','HTTP2 in Action.pdf','EAction.pdf','268f6fc8938d61e515dcb4bf15ed8352'),('c2aa98f1-1da7-11ea-b5b5-72c94ee665bd','the road less traveled.pdf','Ess traveled.pdf','989beea96803c86eb47f80c325f278a8')]
insql = "INSERT INTO `books`(`BookId`, `BookName`, `BookPath`, `Md5`, `CreateDate`) VALUES ('3439bce4-1d9e-11ea-bf4e-72c94ee665bd','Android.4.0.pdf','eee.pdf','0a4de4aab827bb10e4a803bc509e9d02',CURRENT_TIMESTAMP())"

def writeToDb(sql,paras):
    try:
        conn = pymysql.connect("localhost","root","123456","books")
        cursor = conn.cursor()
        cursor.executemany(sql,paras)
        # cursor.execute(insql)
        conn.commit()
        conn.close()
    except:
        print("Error promed") 

if __name__=='__main__':
    writeToDb(sqlbase,data)

# try:
#     # cursor.execute(sql)

#     insql = "INSERT INTO `BOOKS`(`BookId`, `BookName`, `BookPath`, `Md5`, `CreateDate`) VALUES ('3439bce4-1d9e-11ea-bf4e-72c94ee665bd','Android.4.0网络编程详解.pdf','F:\/books\/Andriod\/Android.4.0网络编程详解.pdf','0a4de4aab827bb10e4a803bc509e9d02',CURRENT_TIMESTAMP());INSERT INTO `BOOKS`(`BookId`, `BookName`, `BookPath`, `Md5`, `CreateDate`) VALUES ('345431b4-1d9e-11ea-836d-72c94ee665bd','Android_Application_Development_For_Dummies.pdf','F:\/books\/Andriod\/Android_Application_Development_For_Dummies.pdf','9a28b5be639db847171a595cb344edd0',CURRENT_TIMESTAMP());"

#     # result = cursor.fetchall()
#     # for row in result:
#     #     id = row[0]
#     #     name = row[1]
#     #     print("id=%s,name=%s" % (id,name))

#     cursor.executemany(sqlbase,data)
#     db.commit()
# except:
#     print("Error: unable to fetch data")

# db.close()
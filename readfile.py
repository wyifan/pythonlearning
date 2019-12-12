import sys
import hashlib
import importlib

#reload(sys)
#sys.setdefaultencoding("utf-8")
importlib.reload(sys)

if __name__=='__main__':
    content="hello world4"
    hash1 = hashlib.md5()
    hash1.update(content.encode("utf-8")) 
    print(hash1.hexdigest())

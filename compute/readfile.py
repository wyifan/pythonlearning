namehandle = open('../kids','w')
namehandle.write("Michael\n")
namehandle.write("Mark\n")
namehandle.close()
namehandle = open("../kids",'r')
for line in namehandle:
    print "in loop:"
    print len(line)
    print line[:2]
namehandle.close()
x = 25
epsilon =0.01
numGuess = 0
low = min(0.00,x)
high = max(1.0, x)
ans = (high+low)/2

while abs(ans**3 -x)>=epsilon:
    print 'low:',low,"high:",high,"ans:",ans
    numGuess+=1
    if ans**3< x:
        low = ans
    else:
        high= ans
    ans = (high+low)/2.0

print "Numguess:", numGuess
print ans, "is close to square root of", x

def isIn(a,b):
    if(str(a) in str(b)):
        return True
    else:
        return False

print isIn("wsf","wwsfe")


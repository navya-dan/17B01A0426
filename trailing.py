import math
def factorialtrailing(N):
    r=0
    n=str(math.factorial(N)//(10**trailingzeroes(N)))
    if len(n)>4:
       for i in range(1,6):
           r=int(n[len(n)-i])+r*10
       print(int(str(r)[::-1]))
def trailingzeroes(k):                                                                                                                          
    i=5
    cnt=0
    while k//i>=1:
          cnt=cnt+k//i
          i=i*5
    return cnt
    
factorialtrailing(9)  

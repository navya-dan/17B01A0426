def gcdsequence(N):
    j=0 
    list1=[13]
    for i in range(5,N+1):
        list1.append(list1[j]+gcd(i,list1[j])
        ++j
    print(list1[N-4])
def gcd(n,d):
    if d==0:
       return n
    else:
       return gcd(d,n%d)    
gcdsequence(1000)        

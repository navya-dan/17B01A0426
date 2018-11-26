def harshad():
    sum=0
    for i in range(1,10000):
        j=0
        k=i
        while i>0:
              if i%(sumdigits(i))!=0:
                 j=1
                 break
              else:
                 i=i//10
        if prime(k//sumdigits(k)) and j==0: 
           sum=sum+k
    print(sum)
def prime(k):
    for i in range(2,((k//2)+1)):
        if k%i==0:
           return False
    if k!=1:
       return True
def sumdigits(k):
    return sum(int(n) for n in str(k))
harshad()

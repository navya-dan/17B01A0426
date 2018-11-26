def digitpowersum():
    i=10
    list=[]
    while len(list)<10:
          k=2
          x=sumdigits(i)
          while True:
                if x**k==i:
                   list.append(i)
                if x**k>i or x==1:
                   break
                k=k+1
          i=i+1
    print(list[9])    
def sumdigits(k):
    return sum(int(n) for n in str(k))
digitpowersum()

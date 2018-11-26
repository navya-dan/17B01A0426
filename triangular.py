def triangular():
    n=45
    while True:
          k=n*(n+1)/2
          if factors(k):
             print(k)
             break
          n=n+1
def factors(k):
    if len(filter(lambda i:k%i==0,range(2,(k//2)+1)))>=498:
       return True
    else:
       return False
    

triangular()


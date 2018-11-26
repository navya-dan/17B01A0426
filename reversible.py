def reversible():
    cnt=0
    k=1
    list2=[]
    while k<=9:
          list2.append(k)
          k=k+2
    for n in range(1,100):
        if n%10!=0:
           rev=n+int(str(n)[::-1])
           if rev%2!=0:
              if odd(rev,list2):        
                 cnt=cnt+1
    print(cnt)
def odd(rev,list2):
    list1=[int(i) for i in str(rev)]
    list1=list(set(list1))
    list3=[j for j in list1 if j in list2]
    if len(list1)==len(list3):
       return True
    else:
       return False 
reversible()
          

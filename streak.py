def streak(s,N):
    cnt=0
    for i in range(2,N):
        j=1
        while True:
              if i%j==0:
                 i=i+1
                 j=j+1
              else:
                 if (j-1)==s:
                    cnt=cnt+1
                 break
                   
    print(cnt)
streak(6,1000000)

def idempotents(n):
    for a in range(0,5):
        if (a*a)%n <= ((a+1)*(a+1))%n:
           big=a+1
    if big<n:
       print(big)
idempotents(6)

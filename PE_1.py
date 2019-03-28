def sums(n):
    n = n-1
    a = 3*(n//3) * ((n//3) + 1 ) 
    b = 5*(n//5) * ((n//5) + 1 ) 
    c = 15*(n//15) * ((n//15)+ 1 ) 

    print((a+b-c)//2)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sums(n)
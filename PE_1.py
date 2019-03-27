def sums(n):
    count = 0   
    for num in range(n):
        if num%3 != 0 or num%5!=0:
            count += num
    print(count)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sums(n)
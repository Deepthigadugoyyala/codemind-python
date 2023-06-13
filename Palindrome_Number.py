def pal(n):
    t=n
    r=0
    while(n!=0):
        r=r*10+n%10
        n=n//10
    return t==r
t=int(input())
for _ in range(t):
    a=int(input())
    print(pal(a))
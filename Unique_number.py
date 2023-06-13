n=int(input())
s=str(n)
a=len(s)
b=set(s)
if(a==len(b)):
    print("Unique Number")
else:
    print("Not Unique Number")
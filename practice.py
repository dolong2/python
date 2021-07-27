'''
a=int(input())
coin=0
coin+=a//500
a%=500
coin+=a//100
a%=100
coin+=a//50
a%=50
coin+=a//10
a%=10
print(coin)
'''

'''
from random import *
n,m=input().split()
n=int(n)
m=int(m)
arr=[[0]*n for row in range(m) ]
brr=[10001]*n
for i in range(n):
    for j in range(m):
        arr[i][j]=randint(1,10000)
        if(brr[i]>arr[i][j]):
            brr[i]=arr[i][j]
    print(arr[i])
max=-1
for i in range(n):
    if(max<brr[i]):
        max=brr[i]
print(max)
'''

'''
n,k=input().split()
n=int(n)
k=int(k)
cnt=0
while n!=1:
    if n%k==0:
        n//=k
    else:
        n-=1
    cnt+=1
print(cnt)
'''


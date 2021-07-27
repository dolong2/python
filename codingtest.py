n=input()
n=int(n)
arr=[[0]*2]*n
for i in range(n):
    arr[i][0],arr[i][1]=input().split()
    arr[i][1]=int(arr[i][1])
for i in range(n):
    j=i
    min=101
    while j<n:
        if min>arr[j][1]:
            min=arr[j][1]
            min_index=j
            min_name=arr[j][0]
        j+=1
    temp=arr[i][1]
    arr[i][1]=min
    arr[min_index][1]=temp

    temp=arr[i][0]
    arr[i][0]=min_name
    arr[min_index][0]=temp
for i in range(n):
    print(arr[i][0])
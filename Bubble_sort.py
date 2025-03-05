lis=[4,2,1,5,6,12,8]
n=len(lis)
for i in range(n):
    for j in range(0,n-i-1):
        if lis[j] > lis[j+1]:
            lis[j],lis[j+1]=lis[j+1],lis[j]
print(lis)

#Alternate method 
def bubble_sort(array):
    for i in range(n):
        for j in range(0,n-i-1):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
lis=list(map(int,input("enter the list").split()))
n=len(lis)
bubble_sort(lis)
print(lis)
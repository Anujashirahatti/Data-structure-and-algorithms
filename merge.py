def merge(list):
    if len(list) > 1:
        mid = len(list)//2
        left = list[:mid]
        right = list[mid:]
        merge(left)
        merge(right)
        L=0
        R=0
        k=0
        while L < len(left) and R < len(right):
            if left[L] > right[R]:
                list[k] = right[R]
                R = R+1
            else:
                list[k] = left[L]
                L=L+1
            k=k+1
        while L < len(left):
            list[k] = left[L]
            L=L+1
            k=k+1
        while R < len(right):
            list[k] = right[R]
            R=R+1
            k=k+1
list=list(map(int,input("enter the list").split( )))
merge(list)
print(list)
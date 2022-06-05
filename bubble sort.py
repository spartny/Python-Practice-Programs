alist=eval(input("enter a list:"))
print("original list is:",alist)
n=len(alist)
for i in range(n):
    for j in range (0,n-i-1):
        if alist[j] > alist[j+1]:
            alist[j],alist[j+1]=alist[j+1],alist[j]
print("the list after sorting is",alist)

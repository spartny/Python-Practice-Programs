alist=eval(input("enter list:"))
length=len(alist)
mean=total=0
for i in range(0,length):
    total=total+alist[i]
mean=total/length
print("the given list is:",alist)
print("the mean of the list is", mean)

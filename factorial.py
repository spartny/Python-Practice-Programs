# Program to calculate the factorial of the given user input number.
num=int(input("enter the number"))
fact=1
a=1
while a<=num:
    fact*=a
    a+=1
print("factorial of ",num,"is",fact)

num=int(input('Enter a no:'))
sum_=0
temp=num
while temp>0:
    digit=temp%10
    sum_+=digit**3
    temp//=10
if num==sum_:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")
    

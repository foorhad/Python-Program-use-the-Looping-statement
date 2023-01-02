num = int(input('Enter the value of num: '))
sum=0
while num>0:
    sum+=num%10
    num=num//10
print('Sum of the input digits: ',sum)
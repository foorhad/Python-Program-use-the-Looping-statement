num = int(input('Enter the value of number: '))
sum=0
number=num
while number>0:
    sum+=(number%10)**3  
    number=number//10
if num==sum:
    print(num, 'is Armstrong')
else:
    print(num,'is not Armstrong')
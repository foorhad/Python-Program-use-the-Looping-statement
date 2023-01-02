string = 'International Cricket Council'
vowel=[]
count=0
for i in string:
    if i in 'aeiouAEIOU':
        count+=1
        vowel.append(i)

print('Total vowel in string =',count)
print(vowel, end=', ')


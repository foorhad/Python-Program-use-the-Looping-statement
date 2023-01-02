set=[12,33,22,1,2,33,44,54,15,16,17]
largest=set[0]
lowest=set[0]
for i in set:
    if i>largest:
        largest=i
    if i<lowest:
        lowest=i

print('lowest number=', lowest)    
print('largest number=',largest)
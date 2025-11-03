lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_count=0
odd_count=0
for i in lst:
    if i%2==0:
        even_count+=1
    elif i%2!=0:
        odd_count+=1
print(f'{even_count} even numbers in the list')
print(f'{odd_count} odd numbers in the list')















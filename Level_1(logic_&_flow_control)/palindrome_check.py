num_or_str=input('enter a number or a string: ')
lst=[]
for i in num_or_str:
    lst.append(i)
print(lst)
for ch in range(len(lst)):
    if lst[ch]!=lst[len(lst)-ch-1]:
        print('not palindrome')
        break
    elif lst[ch]==lst[len(lst)-ch-1]:
        print('palindrome')
        break


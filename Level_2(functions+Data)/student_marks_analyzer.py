
def find_topper(dct):
    name=max(dct,key=dct.get)
    return name,dct[name]
print(find_topper({'ram':87,'sita':91,'gopal':78}))
def average(dct):
    total=0
    for i in dct.values():
        total+=i
    return total/len(dct)
avg=average({'ram':87,'sita':91,'gopal':78})
print(avg)
def top_scores(dct):
    toppers=[]
    for key,value in dct.items():
        if value>avg:
            toppers.append(key)
    return toppers
print(top_scores({'ram':87,'sita':91,'gopal':78}))
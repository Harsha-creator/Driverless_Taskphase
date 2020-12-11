my_tuple=(1,2,3,3,5,50,50,5)
result = tuple(set(my_tuple))
res = sum(list(result)) 
def sum(res):
    if tup == ():
        return 0
    if isinstance(tup[0],int):
        return res[0] + sum(res[1:])
    if isinstance(tup[0],tuple):
        return sum(res[0]) + sum(res[1:])
totalsum= sum(res)
print(sum)

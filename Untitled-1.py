
from itertools import *
lines=[]
def sortSecond(x):
    return int(x[1])


with open('C:/Users/Harsha Vardhan/Downloads/names.txt', 'r') as filehandle:
    lines = [line.rstrip().split(",") for line in filehandle.readlines()]

lines.sort(key= sortSecond)
names=""


for i in range(len(lines)):

    if(i%2==1):
        del lines[i:i+1]
for j in range(len(lines)):
    names = names+ lines[j][0] 
Min = 26
duplicate =[]
for letter in names:
    duplicate.extend(letter)

def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 
final = Remove(duplicate)
print(final)
for i in range( len(final)-1):
    for j in range(i+1,len(final)):
        if(abs(ord(final[i])-ord(final[j]))< Min):
            Min = abs(ord(final[i])-ord(final[j]))
print(Min)
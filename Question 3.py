def  convert_to_hex(ascii_value):
    return hex(ascii_value)
lst = [] 
n = int(input("Enter number of elements : ")) 
for i in range(0, n): 
    ele = int(input()) 
    lst.append(ele)
flag = 0
for j in range(0,n/2):
    if(lst[j]!=lst[n-j-1]):
        flag =1
        break
if(flag==1):
    print("not palindrome")
else:
    for k in range(n):
       print( convert_to_hex(ord(lst[k]))
k =0 
for i in range(2*n - 1):
    for j in range(n-k-1):
        print(" ")
     o=0
     for j un range(2*k(:
         print(lst[j])
         if(j<k) :
             o++
         else:
             o--
      print("\n")
      if(i<n-1):
          k++
      else:
          k--

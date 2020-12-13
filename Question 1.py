print("input for A")
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  

A= [] 
print("Enter the entries rowwise:") 
 
for i in range(R):           
    a =[] 
    for j in range(C):       
         a.append(int(input())) 
    A.append(a) 
    
print("input for B")
R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  

B= [] 
print("Enter the entries rowwise:") 
 
for i in range(R):           
    a =[] 
    for j in range(C):       
         a.append(int(input())) 
    B.append(a) 
result = []
def matrixmult(A,B):
    for i in range(len(A)):
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j] 

def transpose(result):
    return [[result[j][i] for j in range(len(result))] for i in range(len(result[0]))] 

lhs = transpose(matrixmult(A,B))
rhs = matrixmult(transpose(B),transpose(A))
if(lhs == rhs):
    print("verified")





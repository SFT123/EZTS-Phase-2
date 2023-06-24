#get one matrix as input display diagonal elements, non diagonal elements, upper diagonal and lower diagonal
r=int(input("Enter no of the rows:"))
c=int(input("Enter no of the columns:"))
matrix=[]
for i in range(r):
    a=[]
    for i in range(c):
        x=int(input("Enter the item:"))
        a.append(x)
    matrix.append(a)
print("The Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
print("The diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i==j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Non diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i!=j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Upper diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i<j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Lower diagonal Elements are:")
for i in range(r):
    for j in range(c):
        if i>j:
            print(matrix[i][j],end=" ")
        else:
            print(" ",end=" ")
    print()
print("The Transpose Matrix is:")
for i in range(r):
    for j in range(c):
        print(matrix[j][i],end=" ")
    print()
# print("The Addition ")





#i = 0
#j = 0
#mat = [i][j]
#r = int(input("Enter the Number of Rows"))
#c = int(input("Enter the no of Comlums"))
#for i in range(0,r):
#    m = int(input("Inputs"))
#    mat.append(m)
#    for j in range(0,c):
#        n = int(input("Inputs"))
#        mat.append(n)
#for i in mat:
#    for j in i:
#        print(j, end=" ")
    
a=[]
b=[]
# multiplication of 2 matrices
n=int(input("Enter the dimension of the Matrix: "))

def mat(dim,lis): # function declaration
    print('Enter entities row wise')
    for i in range(dim):
        row=[]# temporary list , its scope is only the first for loop
        for j in range(dim):
            ent=int(input())
            row.append(ent)
        lis.append(row)
    print()
    print('Current matrix is')

    for i in range(dim): #inorder to print the matrix more visually appealing
        for j in range(dim):
            print(lis[i][j], end=' ')
        print()# for a blank line just for visual appeal

mat(n,a)
print()
mat(n,b)
print()

result=[]# a null matrix which later takes the value of the resultant matrix
for i in range(n):
    row=[]
    for j in range(n):
         row.append(0)
    result.append(row)

#core of the program starts here
for i in range(n):
    for j in range(n):
        for k in range(n):
            result[i][j]+=a[i][k]*b[k][j]

print('Resultant matrix is')
print()
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()

#function to create matrix:-
def create_matrix(row,col):
   #This will create empty list in wich matrix will be added:-
    mat=[]
    for i in range(row):
        new_row=[]#This list is created because it will display entered list in form of proper matrix 
        for j in range(col):
            
            data=int(input(f"Enter the value for {i+1}rows ,{j+1}coloum : "))
            new_row.append(data)
        mat.append(new_row)
    return mat        

#Function to display matrix:-
def display_matrix(mat):
    for rows in mat:
        print(rows)

#Function to add two matrixs:-
def matrix_add(mat1,mat2):
    result=[]
    if len(mat1)!=len(mat2) or len(mat1[0])!=len(mat2[0]):
        return None
    for i in range(len(mat1)):
        row=[]
        for j in range(len(mat1[0])):
            row.append(mat1[i][j]+mat2[i][j])
        result.append(row)
    return result   

def matrix_multiplication(mat1,mat2):
    rows1 = len(mat1)
    cols1 = len(mat1[0])
    rows2 = len(mat2)
    cols2 = len(mat2[0])
    
    if cols1!=rows2:
        return None
    else:
        r_matrix=[[0 for _ in range(cols2)]for _ in range(rows1)] #It will create zero matrix of zise row1*col2(IF you want to create same matrix as given matrix then you need to write coloumb first and then rows , then it will create same matrix as given.)
        for i in range(rows1):
            for j in range(cols2):
                for k in range(cols1):
                    #Simple calculation for matrix multiplication..
                    r_matrix[i][j]+=mat1[i][k]*mat2[k][j]
        return r_matrix 
def matrix_transpose(mat):
   #Here to transpose the given matrix we have created zero matrix of opposite dimension from given matrix 
   mats=[[0 for _ in range(len(mat))]for _ in range(len(mat[0])) ]
   for i in range(len(mat)):
      for j in range(len(mat[0])):
         mats[j][i]=mat[i][j]

   return mats                  
   


print("*"*80)
print("Matrix Calculator:-")
print("*"*80)
while True:
 print("-"*80)
 print('''\tEnter 1 for matrix Addition.
       Enter 2 for matrix Multiplication
       Enter 3 for matrix Transpose    
       Enter 4 for exit''')   
          
 print("-"*80)
 try:
    n=int(input("Enter Your choise : "))
    print(" ")
 except ValueError:
    print("Choise Invalid❌")
    continue   
 
   


 match n:
     case 1:
       try:
        row=int(input("Enter the number of rows :  "))
        col=int(input("Enter the number of coloumb :  "))
        if row<0 or col<0:
            print("Number of row and coloumb should be greater then zero")
            continue
       except ValueError:
        print("Enter only integers!")
        continue
       print("Enter dimension and values for first matrix:--")
       mat1=create_matrix(row,col)
       print("Enter dimension and values for second matrix:--")
       mat2=create_matrix(row,col)
       print("First entered matrix:--- ")
       print("="*70)
       display_matrix(mat1)
       print("="*70)
       print("second entered matrix:--- ")
       print("="*70)
       display_matrix(mat2)
       print("="*70) 
       result=matrix_add(mat1,mat2)
       if result is None:
          print("Matrix Multiplication is not Possibel!")
       else :
          print("Sum of two matrix:-")
          print("="*70)
          display_matrix(result)
          print("="*70)
     case 2:
         print("Matrix Multiplication:---")
         
         print("Enter dimension and values for first matrix:--")
         try:
          row=int(input("Enter the number of rows :  "))
          col=int(input("Enter the number of coloumb :  "))
          if row<0 or col<0:
            print("Number of row and coloumb should be greater then zero")
            continue
         except ValueError:
          print("Enter only integers!")
          continue
         mat1=create_matrix(row,col)
         print("Enter dimension and values for second matrix:--")
         try:
          row=int(input("Enter the number of rows :  "))
          col=int(input("Enter the number of coloumb :  "))
          if row<0 or col<0:
            print("Number of row and coloumb should be greater then zero")
            continue
         except ValueError:
          print("Only enter integers!")
          continue
         mat2=create_matrix(row,col)
         print("="*70)
         print("First entered matrix:--- ")
         display_matrix(mat1)
         print("="*70)
         print("second entered matrix:--- ")
         display_matrix(mat2)
         print("="*70)
         result=matrix_multiplication(mat1,mat2)
         if result is None:
            print("Matrix Multiplication is not possible!")
         else:
            print("Matrix Multiplication:- ")
            print("="*70)
            display_matrix(result)
            print("="*70)   
     case 3:
       try:
          row=int(input("Enter the number of rows :  "))
          col=int(input("Enter the number of coloumb :  "))
          if row<0 or col<0:
            print("Number of row and coloumb should be greater then zero")
            continue
       except ValueError:
          print("Enter Integer only!")
          continue
       mat0=create_matrix(row,col)
       print("Matrix before Transpose:- ")
       print("="*70)
       display_matrix(mat0)
       print("="*70)
       print("Matrix after Transpose::-")
       print("="*70)
       result=matrix_transpose(mat0)
       display_matrix(result)
       print("="*70)
     case 4:
       print("Exited🫡")
       break
     case _:
       print("Please enter choise from given option only")
       continue  

           

            
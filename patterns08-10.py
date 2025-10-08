list1 =[[1,5],
        [7,3]] 
list2 =[[12,-1],
        [0,9]] 

cols = len(list1[0]) 
rows = len(list1) 
res =[]
for i in range(rows):
    row_sum =[]
    for j in range(cols):
            row_sum.append(list1[i][j]+list2[i][j])
    res.append(row_sum)        
print(res)

n = 7
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i + j == n - 1 or i == n//2 or j == n // 2:
            print('*',end =' ')
        else:
            print(' ',end =' ')    
    print()    
print()
n = 7
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == n//2 or j == n//2 :
            print('*',end =' ')
        else:
            print(' ',end =' ')    
    print()   
print()        
n = 7
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 :
            print('*',end =' ')
        else:
            print(' ',end =' ')    
    print()   
n = 7
for i in range(n):
    for j in range(n):
        if j == 0 or j == n -1 or i == 0 or i == n//2:
            print('*',end=' ')  
        else:
            print(' ',end=' ')     
    print()     
print()    
for i in range(n):
    for j in range(n):
        if j == 0 or j == n -1 or i == 0 or i == n//2 or i == n-1:
            if (i == 0 and j == n-1) or (j == n-1 and i == n - 1):
                print(' ',end =' ')
            else:    
                print('*',end=' ')  
        else:
            print(' ',end=' ')     
    print()       
print()

n = 7 
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 :
            if (i == 0 and j == 0) or (j == 0 and i == n -1 ):
                print(' ',end =' ')
            else:    
                print('*',end =' ')
        # else:
        #     print(' ',end =' ')    
    print()        

      
n = 7
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 :
            if (j == n - 1 and i == 0) or (j == n - 1 and i == n -1 ):
                print(' ',end =' ')
            else:    
                print('*',end =' ')
        else:
            print(' ',end =' ')    
    print()        
n = 7
for i in range (n):
    for j in range(n):
        if j == 0 or i == 0 or i == n// 2:
            print('*',end =' ')  
    print() 
print()  

n = 7
for i in range (n):
    for j in range(n):
        if j == 0 or (i == j and i < n//2) or j == n - 1 or (i+j == n-1 and i < n//2 + 1):
            print('*',end =' ')  
        else:
            print(' ',end =' ')    
    print() 
print()
n = 7
for i in range (n):
    for j in range(n):
        if j == 0 or j == n - 1 or i == 0 or i == n - 1 :
            if (i == 0  and j == n - 1) or (i == 0 and j == 0) or (i == n - 1 and j == 0) or  (i == n - 1 and j == n - 1):
                print(' ', end =' ')
            else:
                print('*',end =' ')  
        else:
            print(' ',end =' ')    
    print() 
n = 7
for i in range (n):
    for j in range(n):
        if j == n//2  or i == 0 :
            print('*',end =' ')  
        else:
            print(' ',end =' ')    
    print()      
print()
n = 7
for i in range (n):
    for j in range(n):
        if i +j == n -1  or (i == j and i < n // 2):
            print('*',end =' ')  
        else:
            print(' ',end =' ')    
    print()       

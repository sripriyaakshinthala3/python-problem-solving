n = 7
mid = n // 2
for i in range(n):
    for j in range(n):
        if  i == 0 or i == n -1 or (i == mid)or (j == 0 and i <= mid)  or (j == n - 1 and i >= mid):
            print('*', end =' ')
        else:
            print(' ',end =' ')    
    print()
print()

n = 7
mid = n // 2
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0  or (j == n - 1 and i <= mid) or i == mid  or ( j == i- mid + 1 and i >= mid):

            if (i == 0 and j == n-1) or (i == mid and j == n-1):
                print(' ',end=' ')
            else:    
                print('*',end =' ')
        else:
            print(' ',end =' ')    
    print()
print()
n = 7
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == 0 or j == mid or i == n - 1:    
            print('*',end =' ')
        else:
            print(' ',end =' ')    
    print()    
print()
n = 7
mid == n // 2
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0 or (j == n-1 and i <= mid) or i == mid:
            if (i == 0 and j == n-1) or(i == mid and j == n - 1):
                print(' ',end=' ')
            else:
                print('*',end =' ')    
        else:
            print(' ',end=' ')        

    print()
print()

n = 7
mid = n // 2
for i in range(n):
    for j in range(n):
        if j == 0 or i == 0  or (j == n - 1 and i <= mid) or i == mid  or ( j == i- mid + 1 and i >= mid):

            if (i == 0 and j == n-1) or (i == mid and j == n-1):
                print(' ',end=' ')
            else:    
                print('*',end =' ')
        else:
            print(' ',end =' ')    
    print()
print()    
n = 7
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == 0 or j == mid or i == n - 1:    
            print('*',end =' ')
        else:
            print(' ',end =' ')    
    print()    
print()
print()
n = 7
mid = n // 2
for i in range(n):
    for j in range(n):
        if (i == j and i < mid)  or i +j == n- 1:    
            print('*',end =' ')
        else:
            print(' ',end =' ')    
    print()    
print()
print()
n = 7
mid = n // 2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n - 1 or i == mid:    
            print('*',end =' ')
        else:
            print(' ',end =' ')    
    print()    
print()
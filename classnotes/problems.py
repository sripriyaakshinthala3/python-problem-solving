#on 22/08/2025 patterns square

# n = 5 
# for i in range(1, n+1):
#     for j in range(1,i+1):
#         print("*", end =" ")
#     print()  

# for i in range(1,n+1):
#     for j in range(1,n-i+2):
#         print("*",end = " ") 
#     print()       

# for i in range(1,n+1):
#     print("* " * i)

# for i in range(n,0,-1):
#     print("* "* i)
# n =5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#     print()  
# n =5      

# n = 5
# for i in range(1,n+1):
#         if i == 1 or i == n:
#             print("* "* n)
#         else:
#             print("* "+ "  "*(n-2) +"*")   

#before 22/08

# for i in range(1,101):
#     print(i)


# n = int(input("enter a number : "))
# sum_n = n * (n+1) // 2
# print("sum of first",n , "natural numbers is : ",sum_n)



# while True:
#     print("1. square")
#     print("2.cube")
#     print("3. EXit")

# select = int(input("enter an opt from select(1-3): "))
# if select == 1:
#     n = int(input("enter a number to square"))
#     print(n**2)
# elif select == 2:
#     n = int(input("enter a number to cube: "))
#     print(n*3)   
# elif select == 3:
#     print("bye") 
#     break    
# else:
#     print("invalid optn enter from given optn ")

#26/08--------------------armstrong-------------------
# n = int(input("enter a number")) #123
# count = 0
# copy_n= n
# while n > 0:
#     count += 1
#     n //= 10
# n = copy_n
# sum = 0
# while n > 0:
#     digit = n % 10
#     sum += digit ** count
#     n //= 10
# if sum == copy_n:
#     print("armstrong number")
# else:
#     print("not an armstrong")    

#We’ll check if 6 is a perfect number.

# n = int(input("enter a number: "))

#to Check Perfect Number 28/08

# n = int(input("enter a number"))
# sum_of_divisors = 0
# for i in range(1,n):
#     if n % i == 0:
#         sum_of_divisors += i
# if sum_of_divisors == n:
#     print(n,"is a perfect number") 
# else:
#     print(n,"is not a perfect number") 

#find all perfect numbers between 1 and 100

# for n in range(1,101):
#     sum_of_divisors= 0
#     for i in range(1,n):
#         if n % i == 0:
#             sum_of_divisors += i
#     if sum_of_divisors == n:        
#         print(n,end =" ")
  
#29/08 scope

num1 = 10  #-> global scope
def test_function():
    num1 = 20  #->local scope
    print(num1)

test_function()
print(num1) 

num1 = 10    # -> global scope
def test_function():
    num1 = 20            #->enclosed scope to inner function
    def inner_function():
        # num1 = 45
        print(num1)      #->local scope of inner_function
    inner_function() 
        
    print(num1)          #->20 local scope of test-function 

test_function()
print(num1) 

num1 = 10  
def test_function():
    global num1          #work on global num1/ to change global 
    num1 = 20
    print(num1)

test_function()
print(num1) 

# we can change global in inner function in 2 ways

num1 = 10  
def test_function():
    # global num1    
    num1 = 20
    globals()['num1'] = 50  #->method 2 to change or work on global scope num1
    print(num1)

test_function()
print(num1) 

num1 = 10  
def test_function():
    num2 = 20
    def inner_function():
        nonlocal num2     #->can change enclosed scope  
        num2 = 45
        print(num2)
    inner_function()   
    print(num2)
test_function()   

#swap
def swap():
    global a
    global b
    a,b = b,a

a = 10
b = 20
swap()
print(a,b)


num1 = 10  
def test_function():
    # global num1    
    # num1 = 20
    globals()['num1'] = 50  #->method 2 to change or work on global scope num1
    print(num1)

test_function()
print(num1) 

#02/09
#built-in functions
#len
def lenn():
    c = 0
    for n in nums:
        c += 1
    return c    
nums =[1,2,3,4]    
print(lenn())   


num = [1,2,3,4,5]
num.append(6)                #->t0 add an element to list use append 
print(num)                    #->list_name.append(val)


num = [1,2,3,4,5]
num.remove(5)                           #list_name.remove(val)
num.remove(num[3])                      #->4 remove
# num.remove(6)                         #-> throws error val not in list
# num.remove()   
# num.remove(2,3)                       #->cann't remove 2 elements from list


# num = [1,2,3,4,5]                       #list_name.pop(index),list.pop()

# print(num.pop())                               #->len(num)-1
# print(num.pop(2))

num = [2,1,3,2,3,2]

for i in num[:]:
    if i == 2:
        num.remove(i)
print(num)    

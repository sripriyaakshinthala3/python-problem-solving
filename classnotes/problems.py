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

#to Check Perfect Number

n = int(input("enter a number"))
sum_of_divisors = 0
for i in range(1,n):
    if n % i == 0:
        sum_of_divisors += i
if sum_of_divisors == n:
    print(n,"is a perfect number") 
else:
    print(n,"is not a perfect number") 

#find all perfect numbers between 1 and 100

for n in range(1,101):
    sum_of_divisors= 0
    for i in range(1,n):
        if n % i == 0:
            sum_of_divisors += i
    if sum_of_divisors == n:        
        print(n,end =" ")
  


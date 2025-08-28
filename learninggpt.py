
#1. Print numbers from 1 to 5 using a while loop.
# n = 1
# while n <= 5:
#     print(n)
#     n += 1

#2. Find the sum of numbers from 1 to 20 using a while loop
# start = 1
# sum = 0
# while start <=20:
#     sum += start
#     start += 1
# print (sum)
    
#3. Count the even numbers between 10 and 50.
# start = 10
# count = 0
# while start <= 50:
#     if start % 2 == 0:
#         count += 1
#         print(start)  
#     start += 1   
# print(count)    

#4. Count the odd numbers between 1 and 100.
# count = 0 
# start = 1
# while start <= 100:
#     if start % 2 ==1:
#         count += 1
#         print(start)
#     start += 1
# print(count)  

#5. Print the multiplication table of 7 (1 to 10).
# n =1
# while n <= 10:
#     print("7 x",n , "=", 7 * n)
#     n += 1
    
#6. Print all digits of 9876 in reverse order. and also count  
# n = 9876
# count = 0
# rev = 0
# while n > 0:
#     digit = n % 10 
#     count += 1
#     rev = rev * 10 + digit
#     n = n // 10
# print(count) 
# print(rev)   

#7. Count the number of digits in 1234567.
# n = 1234567
# str_n = str(n)
# print(len(str_n))

# sum = 0
# for i in str_n:
#     sum += int(i)

# print(sum)

#---------------------METHOD-2--------------------------------
# n = 1234567
# count = 0
# while n > 0:
#     digit = n % 10
#     count += 1
#     n = n // 10
# print(count)    


#8. Sum only odd digits of 24681357.
# n = 24681357
# sum = 0
# while n > 0:
#     digit = n % 10
#     if n % 2 == 1:
#         sum += digit
#     n = n // 10
# print(sum)  

#9. Stop printing numbers when the sum of numbers becomes more than 50 (start from 1).
# start = 1
# sum = 0  
# while start <= 50:
#     sum += start
#     print(sum)
#     if sum > 50:
#         break
#     start += 1 
    
#10. Print numbers from 20 down to 1 in reverse using a while loop.    
# start = 20
# while start >= 1:
#     print(start)
#     start -= 1

#using for
# for i in range(20,0,-1):
#     print(i)

#----------------METHOD 1 OF WRITING IS n PRIME NUMBER---------------------------------
# n = 13
# if n <= 1:
#     print("Not a prime")
# else: 
#     is_prime = True
#     for i in range(2,n):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(n,"is a prime number")
#     else:
#         print(n,"is not a prime number")    



#----------------METHOD 2 OF WRITING IS n PRIME NUMBER ? using count---------------------------------
# n = 37
# count = 0
# for i in range(1,n+1):
#     if n % i == 0 :
#         count += 1

# print("prime") if count == 2 else print("not aprime")

#----------------METHOD 3 OF WRITING IS num1  PRIME NUMBER? USING FUNCTIONS---------------------------------

# def check_prime(num1):
#     if num1 <= 1:
#         return "not a prime"
#     for i in range(2, num1):
#         if num1 % i == 0:
#             return " not a prime"
#     return "prime"   

# print(check_prime(25))


#----------------METHOD 4 OF WRITING  IS num1  PRIME NUMBER------------------------------
# def is_prime(num1):
#     if num1 <= 1 :
#         return False
#     for i in range(2,int(num1 ** 0.5)+1):
#         if num1 % i == 0:
#             return False
#     return True
# print(is_prime(29))

#----------------METHOD 5 PRIME NUMBER---------------------------------
# n = int(input("enter a number: "))
# if n > 1:
#     for i in range(2,n):
#         if n % i == 0:
#             print(n,"Not prime")
#             break
#     else:
#         print(n, "is prime")
# else:
#     print(n,"Not prime") 

# -------------------------------------------------------------------------------------------------------------------------------------
#ii)Reverse only the first 3 digits.------------------

# num = 12345
# first_three = num // 100 
# last_two = num % 100

# rev = 0
# while first_three > 0:
#      rev = rev * 10  + first_three % 10
#      first_three //= 10

# result = rev * 100 + last_two
# print(result)
#----------------------------------------------------------------------------------------------------------------------
#Find sum of digits until it becomes a single digit (digital root).
# num = 1234
# while num >= 10:
#     sum_digit = 0
#     while num > 0:
#         digit = num % 10
#         sum_digit += digit 
#         num //= 10
#     num = sum_digit 

# print(num)
#-------------------------------------------------------------------------------------------------------------------------
#Check if a number is Harshad (divisible by sum of digits).

# sum = 0
# num = 18
# copy_num = num

# while num > 0:
#     digit = num % 10
#     sum += digit 
#     num = num // 10


# if copy_num % sum == 0:
#     print('Harshad number')
# else:
#     print("not a Harshad number")    
#---------------------------------------------------------------------------------------------------------------------------------
#Find the product of digits instead of sum.
# num = 123
# product = 1
# while num > 0:
#     digit = num % 10
#     product = product * digit
#     num //= 10

# print(product)
#--------------------------------------------------------------------------------------------------------------------------------
# find a number is prime or not

# n = int(input("enter a number"))
# if n <= 1:
#     print("not a prime number")
# else:
#     is_prime = True
#     for i in range(2,n):
#         if n % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(n ,"is prime number")
#     else:
#         print(n,"is not a prime number")
#----------------------------------------------------------------------------------------------------------------------------------
#level iii)Check if the reverse of a number is prime.

# n = 123
# copy_n = n
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10  
# if rev > 1:
#     for i in range(2, rev):
#         if rev % i ==0: 
#             print("reverse of ", copy_n , " is  not a prime")   
#             break
#     else:
#         print("reverse  of ", copy_n , " prime")     
# else :
#     print("reverse of ", copy_n , " is  not a prime")
#---------------------------------------------------------------------------------------------------------
#Find the largest digit in the number.
# n = 23875
# largest = 0 
# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         largest = digit 
#     n //= 10

# print("largest digit in n is",largest)

# ---------------------------------METHOD 2--------------------------------------------------------------------------------------

# largest = 0 
# for i in "23875":
#     digit = int(i)
#     if digit > largest:
#         largest = digit
# print(largest)        
#----------------------------------------------------------------------------------------------------------------------------
#Check if digits are in increasing order (e.g., 1234 ✅, 4321 ❌).
n = 345
order = -1 
increasing = True
while n > 0:
    digit = n % 10
    if digit <= order:
        increasing = False
        break
    order = digit
    n //= 10
if increasing:
    print("digits are in increasing order")
else:
    print("digits are not in increasing order") 
#------------------------------------------------------------------------------------------------------------------
n = input("enter a number: ")
increasing = True 
for i in range(len(n)-1):
    if int(n[i]) >= int(n[i+1]):
        increasing = False
        break

if increasing:
    print("digits are in increasing order")    
else:
    print("digits are not in increasing order")
#---------------------------------------------------------------------------------------------------------    

# n = int(input("enter a number: "))
# if n > 1:
#     for i in range(2,n):
#         if n % i == 0 :
#             print(n,"is not a prime")
#             break
#     else:
#         print(n,"is prime")

# else:
#     print(n,"is not a prime")
#-------------------------



 


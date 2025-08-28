# def can_form_triangle(a,b,c):
#     if a + b > c and a + c > b and b + c > a:
#        if a == b == c:
#         return "equilateral"
#        elif (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
#         return "right angled triangle"
#        elif a == b or b == c or a == c:
#         return "isoscales triangle"
#        else :
#         return "can form a scalene triangle -no side is equal "
#     return "cannot form a triangle with provided sides"


# a = int(input("enter side a: "))
# b = int(input("enter side b: "))
# c = int(input("enter side c: "))
# print(can_form_triangle(a,b,c))        

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
#             print(n,"Not a prime")
#             break
#     else:
#         print(n, "is prime")
# else:
#     print(n,"Not prime") 

# -------------------------------------------------------------------------------------------------------------------------------------  
# Using a for loop and range, print only the prime numbers between 100 and 300.assignment(25/08)

# start = 100
# end = 300
# print("Prime numbers between",start,"and",end,"are: ")

# for num in range(start,end+1):
#     if num > 1:
#         for i in range(2,int(num ** 0.5)+1):
#             if num % i == 0:
#                 break
#         else:
#             print(num, end =" ")    


 

   




    
 





    




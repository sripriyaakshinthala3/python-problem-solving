#a.  Easy Questions:
#problems  using functions

# i)Write a program to check if a given number is positive, negative, or zero.

def check_sign(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    return "neither positive nor negative" 

number = int(input("enter a number: "))
print(check_sign(number))
#-----------------------------------------------------------------
# ii)Determine if a number is odd or even.

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "odd"

number = int(input("enter a number: "))
print(check_even_odd(number))
#----------------------------------------------------------------
# iii) Check if a person is eligible to vote (age >= 18).
def is_eligibel_to_vote(age):
    if age >= 18:
        return "Eligible to vote"
    return "Not eligible to vote"

age=int(input("Age: "))
print(is_eligibel_to_vote(age))

#----------------------------------------------------------------
#iv) Write a program to find the greatest of two numbers.
def gretest_of_numbers(num1,num2):
    if num1 > num2:
        return str(num1) + " is greater"
    elif num2 > num1:
        return str(num2) + " is greater"
    return "both are equal"

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
print(gretest_of_numbers(num1,num2))
#----------------------------------------------------------------
# v)Write a program to find the greatest of two numbers.
# Print "Pass" if a student scores more than 40 marks;
#  otherwise, print "Fail."
def check_result(score):
    if score > 40:
        return "Pass"
    return "Fail"

score=int(input("score: "))
print(check_result(score))
#----------------------------------------------------------------
# vi)Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).
def day_of_a_week(n):
    days =["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
    if 1 <= n <=7:
        return days[n-1]
    else:
        return "Invalid input"
n = int(input("enter a number(1-7): "))
print(day_of_a_week(n))
#----------------------------------------------------------------

# vii)Implement a simple calculator to perform addition, subtraction, multiplication, and division.
def simple_calc(num1,num2,op):
    if op == "+":
        return num1+num2
    elif op == "-":
        return num1-num2
    elif op == "*":
        return num1*num2
    elif op == "/" :
        if num2 != 0:
            return num1/num2
        return "cannot divide by zero"  
    else:
        return "invalid op"

num1=int(input("enter first number: "))
num2=int(input("second number: "))    
op=input('enter an op(+,-,*,/):')    
print(simple_calc(num1,num2,op))
#----------------------------------------------------------------
#viii)Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.).
def month_from_number(n):
    months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
    if  1 <= n <= 12:
        return months[n-1]
    return "invalid input"

n = int(input("enter a number (1-12): "))
print(month_from_number(n))
#----------------------------------------------------------------

#b. Medium Questions:
# i)Write a program to find the greatest of three numbers.
def gretest_of_numbers(num1,num2,num3):
    if num1 == num2 == num3:
        return "all three numbers are equal"
    elif num1 >= num2 and num1 >= num3:
        if num1 == num2:
            return str(num1) + " and " + str(num2) + " are equal "   
        elif num1 == num3:
            return str(num1) + " and " + str(num3) + " are equal"   
        return str(num1) + " is gretest"
    elif num2 >= num1 and num2 >= num3:
        if num2 == num1:
            return str(num1)+ " and " + str(num2) + " are equal"
        elif num2 == num3:
            return str(num1) + " and " + str(num3) + " are equal" 
        return str(num2) + " is gretest"
    elif num3 >= num1 and num3 >= num2:
        if num3 == num1:
            return str(num3)+ " and " + str(num1)+ " are equal"
        elif num3 == num2:
            return str(num1) + " and " + str(num3) + " are equal"    
        return str(num3) + " is gretest"   
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
num3=int(input("enter third  number: "))
print(gretest_of_numbers(num1,num2,num3))
#----------------------------------------------------------------

#ii)Check if a year is a leap year.
def check_leap(year):
    if (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0):
        return "Leap year"
    return "Not a leap year"    

year = int(input("enter a year: "))
print(check_leap(year))
#----------------------------------------------------------------

#iii)Write a program to classify a character entered by the user as a vowel, consonant, or neither.
def classify_character(character):
    if character in "aeiouAEIOU":
        return "vowel"
    elif character  not in "aeiouAEIOU":
        return "Consonant" 
    return "neither"      

character = input("enter a character: ")
print(classify_character(character))

#modified from class 19-08-2025
def classify_character(character):
    if len(charcter)!=1:
        return "Invalid input"
    elif character in "aeiouAEIOU":
        return "vowel"
    elif character.isalpha():
        return "consonant"
    return "neither"  

character = input("enter a character: ")
print(classify_character(character))    
#----------------------------------------------------------------

# iv) Calculate the grade of a student based on the marks they score: 
# 1. 90-100 : Grade A
# 2. 80-89 : Grade B 
# 3. 70-79 : Grade C 
# 4. <70 : Fail.

def calc_grade(marks):
    if 90 <= marks <= 100:
        return "Grade A" 
    elif 80 <= marks <= 89:
        return "Grade B"   
    elif 70 <= marks <=79:
        return "Grade C"
    return "Fail"         

marks = int(input("enter marks: "))
print(calc_grade(marks))
#----------------------------------------------------------------
#Write a program to check if three sides length form a valid triangle.
def can_form_triangle(side1,side2,side3):
    if (side1>0 and side2>0 and side3>0) and (side1 + side2 > side3 and side1 + side3 > side2 and side2 +side3 >side1):
        return  "Forms a valid triangle"
    return "cannot form a triangle"

side1= int(input("enter first side: "))
side2 = int(input("enter second side: "))
side3= int(input("enter third side: "))
print(can_form_triangle(side1,side2,side3))
#----------------------------------------------------------------
#LOOPS CONCEPT
#i)Print all numbers from 1 to 100 using a for loop.

def print_numbers(n):
    for i in range(1,n+1):
        print(i)
print_numbers(100)


#ii)Write a program to print the sum of the first n natural numbers. (n*n+1/ 2)
def sum_numbers(n):
    print((n * (n + 1))/2)
sum_numbers(int(input("enter a number: ")))
#----------------------------------------------------------------

#iii)Print all even numbers between 1 and 50 using a while loop.

def even_numbers(a,n):
    while a < n+1:
        if a % 2 == 0:
            return a
print(even_numbers(1,50))
 
#--------------------------------------------------------------------------

#iv. Write a program to display the multiplication table of a given
#number. First 20

def multiplication_table(n):
    for i in range(1,21):
        print(n ," x " ,i ," = ", n*i)

n = int(input("enter a number: "))
(multiplication_table(n))

#-------------------OR-------------------------------------------

def multiplication_table(n):
    table =[]
    for i in range(1,21):
        table.append(n + " x " + str(i) + " = " + str(int(n)*i))
    return table

n = input("enter a number: ")
result=multiplication_table(n)
for line in result:
    print(line)

#----------------------------------------------------------------------

#v. Reverse a number using a while loop.
#1. Also can we get the sum of all the digits

n = int(input("enter a number:  "))
rev = 0
sum_n = 0
while n > 0:
    digit = n % 10
    sum_n = sum_n + digit
    rev = rev * 10 + digit
    n = n // 10

print(rev)
print(sum_n)

#--------------------------------------------------------------------------

#vi. Write a program to count the number of digits in a given
#number using a while loop.-------METHOD-1-----------------

given_n=int(input("enter a number:  "))
count = 0
rev_n=0
while given_n > 0:
    digit = given_n % 10
    count += 1      
    given_n= given_n // 10

print(count)

# ------------METHOD-2-------------------------------

n = 123
str_n=str(n)   
print(len(str_n))   

sum=0
for i in str_n:
    sum += int(i)
print(sum)    

#--------------------------------------------------------------------
#vii. Write a program that keeps asking the user to enter numbers
#until they enter a negative number. Use a while loop

while True:
    user_input = int(input("enter a number"))
    if user_input < 0:
        break

#------------------------------------------------------------------------
#b. Medium Questions:
#i. Print the first 10 terms of the Fibonacci series using a for
#loop.  
#--------------------------------------------------------------------------
#ii. Check if a given number is a prime number using a for
#loop.
#-------------------------------------------------------------------------
#iv. Print all numbers from 1 to 100 that are divisible by 3 and 5
#using a for loop.

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
#----------------------------------------------------------------------------
#v. Implement a menu-driven program where the user can
#choose to:
#1. Find the square of a number.
#2. Find the cube of a number.
#3. Exit.

while True:
    print('1.Square  2.Cube  3.Addition  4.Subtraction  5.Multiplication  6.Division  '  )
    choice = input("Enter your choice: ")

    if choice == '1' or choice == 'Square':
        input_num = int(input("enter a number: "))
        print(input_num ** 2)
    elif choice == '2' or choice == 'Cube': 
        input_num = int(input("enter a number: "))
        print(input_num ** 3)
    elif choice == '3' or choice == 'Addition':
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second  number: "))
        print(num1 + num2)
    elif choice == '4' or choice == 'Subtraction':
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second  number: "))
        print(num1 - num2)
    elif choice == '5' or choice == 'Multiplication ':
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second  number: "))
        print(num1 * num2)
    elif choice == '6' or choice == 'Division ':
        num1 = float(input("enter first number: "))
        num2 = float(input("enter second  number: "))
        if num2 == 0:
            print("cannot divide by zero ")
        else :
            print(num1 / num2) 
            break
    else:
        print('No valid option picked')
        print('Exit....')  

#-----------------------------------------------------------------------------
#vi. Implement a basic login system where the user has three
#attempts to enter the correct password using a loop

db_Username = "admin123"
db_Password = "admin@123"
attempts = 3

while attempts > 0:
    input_username = input('enter username: ')
    input_password = input('enter password: ')

    if db_Username ==  input_username and  db_Password == input_password :
        print("Login success")
        break
    else:
        attempts -= 1
        print("Login failed")

#------------------------------------------------------------------------------



    


                

     
            
            
        
            










# n= int(input("enter a number"))
# count=0
# sum_n=0
# while n > 0:
#     digit = n % 10
#     sum_n = sum_n + digit
#     count += 1
#     n = n // 10


# print(count)  
# print(sum_n)  

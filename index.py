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
 
# ii)Determine if a number is odd or even.

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    return "odd"

number = int(input("enter a number: "))
print(check_even_odd(number))

# iii) Check if a person is eligible to vote (age >= 18).
def is_eligibel_to_vote(age):
    if age >= 18:
        return "Eligible to vote"
    return "Not eligible to vote"

age=int(input("Age: "))
print(is_eligibel_to_vote(age))


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

# v)Write a program to find the greatest of two numbers.
# Print "Pass" if a student scores more than 40 marks; otherwise, print "Fail."
def check_result(score):
    if score > 40:
        return "Pass"
    return "Fail"

score=int(input("score: "))
print(check_result(score))

# vi)Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).
def day_of_a_week(n):
    days =["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]
    if 1 <= n <=7:
        return days[n-1]
    else:
        return "Invalid input"
n = int(input("enter a number(1-7): "))
print(day_of_a_week(n))

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

#viii)Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.).
def month_from_number(n):
    months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
    if  1 <= n <= 12:
        return months[n-1]
    return "invalid input"

n = int(input("enter a number (1-12): "))
print(month_from_number(n))


#b. Medium Questions:
#i)Write a program to find the greatest of three numbers.
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



#ii)Check if a year is a leap year.
def check_leap(year):
    if (year % 4 ==0 and year % 100 !=0) or (year % 400 ==0):
        return "Leap year"
    return "Not a leap year"    

year = int(input("enter a year: "))
print(check_leap(year))


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

#Write a program to check if three sides length form a valid triangle.
def can_form_triangle(side1,side2,side3):
    if (side1>0 and side2>0 and side3>0) and (side1 + side2 > side3 and side1 + side3 > side2 and side2 +side3 >side1):
        return  "Forms a valid triangle"
    return "cannot form a triangle"

side1= int(input("enter first side: "))
side2 = int(input("enter second side: "))
side3= int(input("enter third side: "))
print(can_form_triangle(side1,side2,side3))
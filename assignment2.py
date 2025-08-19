def can_form_triangle(a,b,c):
    if a + b > c and a + c > b and b + c > a:
       if a == b == c:
        return "equilateral"
       elif (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2):
        return "right angled triangle"
       elif a == b or b == c or a == c:
        return "isoscales triangle"
       else :
        return "can form a scalene triangle -no side is equal "
    return "cannot form a triangle with provided sides"


a = int(input("enter side a: "))
b = int(input("enter side b: "))
c = int(input("enter side c: "))
print(can_form_triangle(a,b,c))        



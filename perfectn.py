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
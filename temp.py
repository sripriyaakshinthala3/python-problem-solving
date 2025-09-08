# #02/09
# nums = [1,2,3,4]
# squares = []
# for n in nums:
#     squares.append(n**2)
# print(squares)    

# nums = [1,2,3,4]
# squares =[n **2 for n in nums]
# print(squares)

# nums = [1,2,3,4]
# squares = list(map(lambda x:x**2,nums))
# print(squares)


# nums =[1,2,3,4,5,6]
# squares_even =list(map(lambda x : x **2,filter(lambda x: x % 2 == 0,nums)))
# print(squares_even)

# nums =[1,2,3,4,5,6]
# squares = [n ** 2 for n in nums if n%2 ==0]
# print(squares)
         
# evens =[n  for n in nums if n%2 ==0]
# print(evens)

# class Car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color
#     def start(self):
#         print(f"{self.color} {self.brand} car is starting....")
#     def stop(self) :
#         print(f"{self.color} {self.brand} car is stopping.....")   

# car1 = Car("honda","red")
# car2 = Car("swift","white")
# print(car1.brand,car2.brand)
# car1.start()
# car2.stop()

a = [1,2,3,4]
print(a[::-1])  #[4, 3, 2, 1]

num1 = [1,2,3,4]
print(num1[2])   #3
#print(num1[4])   #list index out of range
print(num1[2:]+num1[:2]) #[3, 4, 1, 2]


print(len(num1)) #4
print(1 in num1)  #True

n1 = [1,2,3]
n2 = [3,4,5] 
print(n1+n2)   #[1, 2, 3, 3, 4, 5]

n1.extend([4,5]) 
print(n1)       #[1, 2, 3, 4, 5]    

n2.append(6)     
print(n2)        #[3, 4, 5, 6]   

n2.insert(4,7)
print(n2)        #[3, 4, 5, 6, 7]

n3 = [1, 2, 3, 3, 4, 5]
n3.remove(3)
print(n3)    #[1, 2, 3, 4, 5]

n =[1, 2, 3, 4, 5]
n.pop(1)
print(n) #[1, 3, 4, 5]
n.pop()
print(n) #[1, 3, 4]

print(n.index(3)) #1
n.reverse()
print(n)

numbers =[1,2,3]
numbers.sort(reverse=True)
print(numbers)  #[3, 2, 1]

numbers.clear()
print(numbers)   #[]

s ={1,2}
s.add(3)
print(s) 

s = {1,2,3}
s.remove(2)
# s.remove(8) #key error
print(s)

s = {1,2,3}
s.discard(2)
# s.discard(8) #->doesn't raise error
print(s)

s = {1,2,3}
print(s.pop()) #1
print(s.pop())  #2
print(s) #{3}

s1 = {1,2}
s2 = {2,3}
print(s1.union(s2)) #{1,2,3}
print(s1.intersection(s2))
print(s1-s2) #{1}
print(s2-s1) #{3}

print(s1.symmetric_difference(s2)) #{1, 3}
print(s1^s2)  #{1, 3}


s1 = {1,2}
s2 = {2,1,4}
print(s1.issubset(s2)) #True
print(s1.issuperset(s2)) #False
print(s2.issubset(s1)) #False
print(s2.issuperset(s1)) #True


s1 = {1,2}
s2 = {3,4}
s3 = {2,3,4}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))















#05-09
#built-in functions
arr =[1,2,3]
print(arr.index(2))
s ="1"#"hi"
print(s*3)

s = " hello, world!  "
print(s.strip()+ "hi")
print(s + "hi")
c =(s.split(","))
print(c)
print("".join(c))

u = "riyapvt"
print(u.upper())
print(u)

r = "i love python"
print(r.replace("python","maths"))
print(r)

cnt = "malayalam"
print(cnt.count("a"))
print(cnt.count("la"))

sstr = "hello"
c = sstr.startswith("h")

#set
can be a tuple,cannot  add list 
s ={1,2,3}
s.remove(2)
s.discard(3)
print(s) 

set ={100, 200, 300, 400}
print(set.pop())
print(set)
set.pop()
print(set)

s1 ={1,2}
s2 ={2,3}
print(s1.union(s2))

tup1 =(1,2,3,4)
tup1 =(5,6)
print(tup1.union)

a = [10,20,30,40,50]
print(a[0],a[-1])
a[2] = 99
print(a)
a.append(60)
# print(a)
a.remove(a[1])
a.pop(1)
print(a)
a.remove(20)
print(a)
del a[1]
print(a)
print(len(a))
print(a[1:4])
print(a[::-1])
print(max(a))
print(min(a))
print(sum(a))
print(sorted(a))
a.sort()
print(a)
a = [1,2,3,4]
print(a[::-1])  #[4, 3, 2, 1]

#07-09

s = "Python"
print(s[0])
print(s[-1])
print(s[:-3])
print(s[:3])
print(s[0:3])
print(s[::])
print(s[::-1])

s1 = "sri"
s2 = "priya"
s3 ="akshinthala"
print(s1+s2+" "+s3)

s1 = "hi"
print(s1*3)

s1 =" hi"
print(s1)
print(s1.strip())

s1 = "hey iam a new user"
print(s1.find("m"))

s1 ="hi hi iam a new student"
print(s1.replace("hi","hey"))
print(s1)

s1 = "hi iam sripriya"
print(s1.split())      #["hi","iam","sripriya"]
new =s1.split()        #["hi","iam","sripriya"]
print(new[0])          #h

items =["1","2","3"]
print(",".join(items)) # "1,2,3"

txt = "apple"
print(txt.count("a"))   #1

txt = "apple" 
print(txt.count("d"))  #0
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
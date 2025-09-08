# arr =[1,2,3]
# print(arr.index(2))
# s ="1"#"hi"
# print(s*3)

# s = " hello, world!  "
# print(s.strip()+ "hi")
# print(s + "hi")
# c =(s.split(","))
# print(c)
# print("".join(c))

# u = "riyapvt"
# print(u.upper())
# print(u)

# r = "i love python"
# print(r.replace("python","maths"))
# print(r)

# cnt = "malayalam"
# print(cnt.count("a"))
# print(cnt.count("la"))

# sstr = "hello"
# c = sstr.startswith("h")

#set
# can be a tuple,cannot  add list 
# s ={1,2,3}
# s.remove(2)
# s.discard(3)
# print(s) 

# set ={100, 200, 300, 400}
# print(set.pop())
# print(set)
# set.pop()
# print(set)

# s1 ={1,2}
# s2 ={2,3}
# print(s1.union(s2))

# tup1 =(1,2,3,4)
# tup1 =(5,6)
# print(tup1.union)

a = [10,20,30,40,50]
# print(a[0],a[-1])
# a[2] = 99
# print(a)
# a.append(60)
# # print(a)
# a.remove(a[1])
# a.pop(1)
# print(a)
# a.remove(20)
# print(a)
# del a[1]
# print(a)
# print(len(a))
# print(a[1:4])
# print(a[::-1])
# print(max(a))
# print(min(a))
# print(sum(a))
# print(sorted(a))
# a.sort()
# print(a)

# a = [10,20,30,40,50]
# print(a[::-1])
# left ,right = 0,len(a) -1
# while left < right:
#     a[left],a[right] = a[right],a[left]
#     left += 1
#     right -=1

# print(a)   

# a = [10,20,30,40,50]
# max_val = a[0] 
# for i in range(1,len(a)):
#     if a[i] > max_val:
#         max_val = a[i]
# print("maximum",max_val)

# a = [10,20,30,40,50]
# total = 0
# for i in a:
#     total+=i
# print(total/len(a))

# arr = [1, 2, 3, 4, 5]
# print(arr[-2:]+arr[:-2])

# arr = [12, 35, 1, 10, 34, 1]
# first = max(arr)
# arr.remove(first)
# second = max(arr)
# print(second)

# arr = [10, 20, 4, 45, 99]
# first = second = float("-inf")
# for num in arr:
#     if num > first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         second = num
# print(second)

# arr = [0, 1, 0, 3, 12]
# for num in arr:
#     if arr[num] == 0:
#         num.append(len(arr[]))

#reverse
# a = [1, 2, 3, 4, 5]
# left,right = 0,len(a)-1
# while left < right:
#     a[left],a[right] = a[right],a[left]
#     left += 1
#     right -=1
# print(a)   
 
#max
# a = [3, 1, 7, 4, 2]
# max_val = a[0]
# for i in a:
#     if i > max_val:
#         max_val = i
# print(max_val)    

# min
# a = [3, 1, 7, 4, 2]
# min_val = a[0]
# for i in a:
#     if i < min_val:
#         min_val = i
# print(min_val)      

# a = [2, 4, 6, 8]  
# total = 0
# for i in a:
#     total += i
# print(total)    
# print(total/len(a)) 

#Rotate the array by 2 positions to the right.
# arr = [1, 2, 3, 4, 5]
# print(arr[-2:]+arr[:-2])

#second largest element
# arr = [12, 35, 1, 10, 34, 1]
# first = max(arr)
# arr.remove(first)
# second = max(arr)
# print(second)
# arr = [12, 35, 1, 10, 34, 1]
# first = second = float("-inf")
# for num in arr:
#     if num >first:
#         second = first
#         first = num
#     elif num > second and num != first:
#         second = num
# print(second)            

# arr = [0, 1, 0, 3, 12]
# pos = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         arr[pos],arr[i] = arr[i],arr[pos]
#         pos += 1
# print(arr)

# arr = [0, 1, 0, 3, 12]

# nonzeros = [x for x in arr if x != 0]
# zeros = [0]*(len(arr) - len(nonzeros))
# print(nonzeros +zeros)
    
     













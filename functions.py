# def add(a,b):
#     return a +b    #->using return and with parameters we can reuse later 
# print(add(2,3))

# def add(a,b):
#     print(a+b)     #->without return using parameters
# add(2,3)    

# def add():
#     return "hi"   #->without parameter and with return
# print(add())    

# def greet():
#     print("hi")
#     print("i am sripriya gupta") #without parameters and without return
# greet()  

# def gcd(a,b):
#     if a >= 1  and b >= 1:
#         factor = 1
#         for i in range (2,min(a,b)+1):
#             if a % i == 0 and b % i == 0:
#                 if i > factor:
#                     factor = i
#         return factor        
# print(gcd(24,18))

# def sum_even(*args):
#     sum = 0
#     for i in args:
#         if i % 2 == 0:
#             sum += i
#     return sum        
# print(sum_even(1,2,3,4,5,6,7,8))

# word = "sripriya"
# vowels =""
# for i in word:
#     if i in "aeiouAEIOU":
#         vowels += i
# print(vowels) 

# string = "sripriya"
# print(string[::-1])

# string = "madam"
# rev = string[::-1]
# if string == rev:
#     print("is palindrome")
# else: 
#     print("is not a palindrome")    
  



name = input("enter a word: ")
is_palindrome= True
for i in range(len(name)//2):
    if name[i] != name[len(name)-1 - i]:
        is_palindrome = False
        break
if is_palindrome:
    print(name,"is palindrome")   
else:
    print(name," is not a palindrome")  

# word = "madam"
# print(len(word)) 

# word = "madam"
# count = 0
# for i in range(len(word)):
#     for j in range(i+1,len(word)):
#         if word[i] == word[j] :
#             count+=1
# print(count)

#reverse string without using slice
# word = "table"
# print("reverse of " ,word," is:")
# for i in range(len(word)-1 ,-1,-1):
#     print(word[i],end=" ")

#check a string palindrome use for loop without slicing 

# word = "madam"  
# is_palindrome = True
# for i in range(len(word)//2):
#     if word[i] != word[len(word)-1 - i]:
#         is_palindrome = False
#         break
# if is_palindrome:
#     print(word,"is palindrome")   
# else:
#     print(word,"is not palindrome")      



# for ch in word:
#     if ch not in counts:
#         counts[ch] = 1
#     else:
#         counts[ch] += 1    
# print("character counts:",counts)   


# # 30/08 practice
# #reverse
# word = "python"
# for i in range(len(word)-1,-1,-1):
#     print(word[i],end="")
# print()    


# #palindrome
# word = "malayalam"
# is_palindrome = True
# for i in range(len(word)//2):
#     if word[i] != word[len(word)-1-i]:
#         is_palindrome = False
#         break 
# if is_palindrome:
#     print(word,"is a palindrome")    
# else:
#     print(word,"is not a palindrome")

# #vowels
# name = "sripriya"
# for ch in name:
#     if ch in "aeiouAEIOU":
#         print(ch,end="")  
# print()          

#freq of ch
# word = "parrot"
# freq={}
# for ch in word:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1    
# print(freq)

# #non repeating char
# word = "google"
# freq={}
# for ch in word:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1  

# for ch in word:
#     if freq[ch] == 1:     
#         print(ch) 
#         break       

#duplicate ch and count
# word = "programming"
# freq={}
# for ch in word:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1

# for ch in freq:
#     if freq[ch] > 1:     
#         print(ch,freq[ch])        
      

#first repeating ch      
# word = "google"
# seen = set()
# for ch in word:
#     if ch in seen:
#         print("first repeating ch is:",ch)
#         break
#     else:
#         seen.add(ch)  


#All non-repeating character 
# word = "parrot"
# freq ={}
# for ch in word:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1     

# for ch in freq:
#     if freq[ch] == 1:
#         print(ch)

#String compression
# string = "aaabbc"
# compressed = ""
# prev = string[0]
# count = 1
# for ch in string[1:]:
#     if ch == prev:
#         count += 1
#     else:
#         compressed += prev + str(count)  
#         prev = ch
#         count = 1  
# compressed += prev + str(count)        
# print(compressed)        

#sliding window usage optinal practice
# arr = [2,1,5,1,3,2]
# k = 3

# window_sum = sum(arr[:k])
# max_sum = window_sum

# for i in range(k,len(arr)):
#     window_sum = window_sum - arr[i-k] + arr[i]
#     max_sum = max(max_sum,window_sum)

# print(max_sum) 

#longest without repeating ch  substring

# s = "abcabcbb"
# seen = set()
# left = 0
# max_len = 0

# for right in range(len(s)):
#     while s[right] in seen:
#         seen.remove(s[left])
#         left +=1
#     seen.add(s[right])
#     max_len = max(max_len,right - left +1)  

# print("longest substring length =",max_len) #->3

#print longest substring

# s = "abcabcbb"
# seen = set()
# left = 0
# max_len = 0
# longest = ""

# for right in range(len(s)):
#     while s[right] in seen:
#         seen.remove(s[left])
#         left +=1
#     seen.add(s[right])    

#     if (right - left +1 ) > max_len:      
#         max_len = right - left + 1
#         longest =s[left:right+1]

# print("longest substring =",longest) #->abc

#anagram check
# s = "add"
# l = "dad"

# if len(s) != len(l):
#     print("not an anagram")
# else:
#     l_list = list(l)       #->to remove ch we use list
#     for ch in s:
#         if ch in l_list:
#             l_list.remove(ch)
#         else:
#             print("not an anagram")
#             break    
#     else:
#         print("anagram")

#method2 for anagram check
# s = "add"
# l ="dad"
# if len(s) != len(l):
#     print("not an anagram")
# else:
#     freq_s ={}
#     freq_l ={}

#     for ch in s:
#         freq_s[ch] = freq_s.get(ch,0) + 1    
#     for ch in l:
#         freq_l[ch] = freq_l.get(ch,0 )+ 1

#     if freq_s == freq_l:
#         print("anagram")
#     else:
#         print("not an anagram")    

# day1 
# s = "sripriya"
# freq ={}

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq) 

# s = "add"
# l = "dad"

# if len(s) != len(l):
#     print("not a anagram")
# else:
#     l_list = list(l)    
#     for ch in s:
#         if ch in l_list:
#             l_list.remove(ch)
#         else:
#             print("not anagram")   
#             break 
#     else:
#         print(s ,"and ",l ,"are anagrams")

# s = "attempt"
# is_palindrome = True
# for ch in range(len(s)//2):
#     if s[ch] != s[len(s)-1-ch]:
#         is_palindrome = False
#         break

# if is_palindrome:
#     print(s,"is a palindrome")  
# else:
#     print(s,"is not a paliindrome")    

# s ="abcabcdb"
# longest = ""
# max_len = 0
# left = 0
# seen = set()

# for right in range(len(s)):
#     while s[right] in seen:
#         seen.remove(s[left])
#         left += 1
#     seen.add(s[right])   

#     if (right - left + 1) > max_len:
#         max_len = right - left + 1
#         longest = s[left:right+1]

# print(longest)  

# max sum of substring
arr = [2,3,4,2,6,5]
k = 3

window_sum = sum(arr[:3])
max_sum = window_sum

for i in range(k,len(arr)):
    window_sum = window_sum - arr[i-k] + arr[i]
    max_sum = max(max_sum,window_sum)

print(max_sum)    

#string compression
# string = "aaaabbbcc"
# prev = string[0]
# compressed =""
# count = 1
# for ch in string[1:]:
#     if ch == prev:
#         count += 1
#     else:
#         compressed += prev + str(count)  
#         prev = ch
#         count = 1
# compressed += prev +str(count)       
# print(compressed) 

#string decompression
# s = "a3b2c1"
# i = 0 
# result = ""

# while i < len(s):
#     char = s[i]
#     i += 1
#     num = ""
#     while i < len(s) and s[i].isdigit():
#         num += s[i]
#         i += 1
#     result += char * int(num)
# print(result)    


#substrings topic**new
# s ="abc"                      #->6 substrings ->n*n+1/2
# for i in range(len(s)):
#     for j in range(i+1,len(s)+1):
#         print(s[i:j])

#subsequences
s = "abc"
subsequences =[""]

for ch in s:
    new_list = []
    for sub in subsequences:
        new_list.append(sub+ch)
    subsequences += new_list
print(subsequences)      
#   
#first repeating ch
# s = "abcabd"   #->c
# freq={}

# for ch in s:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1   
# for ch in s:
#     if freq[ch] == 1:
#         print(ch)
#         break


#manual approach to reverse words in string

# s ="I love coding"  #->coding love I
# words = []
# word = ""
# for ch in s:
#     if ch != " ":
#         word += ch
#     else:
#         if word:
#             words.append(word)
#             word =""
# if word:
#     words.append(word)      

# reversed_result = ""
# for i in range(len(words)-1,-1,-1):
#     reversed_result += words[i] + " "
# print(reversed_result.strip())    

# group anagrams **new topic
s ="listen"
l ="silent"

if len(s) != len(l):
    print(s,l ,"are not anagrams")
else:
    list_l=list(l)   
    for ch in s:
        if ch in list_l:
            list_l.remove(ch) 
        else:
            print(s,l,"are not anagrams")  
            break
    else:
        print(s,",",l,"are anagrams")      

# words = ["tan","nat","bat","eat","ate","tea"]   
# groups = {}

# for word in words:
#     key ="".join(sorted(word))
#     if key not in groups:
#         groups[key] =[]
#     groups[key].append(word)   

# result = list(groups.values())   
# print(result) 




     


  



    














      




# check if a number is even or odd
'''logic : if a number gives reminder as 0 when divided by 2 
it is a even number else odd number'''
# n = int(input())
# if(n%2==0):
#     print(f"The number is even:{n}")
# else:
#     print(f"The number is odd:{n}")

#Prime number
'''a number which has only two factors (1 & itself) no other factor'''
# n = int(input())
# i=1
# counter=0
# for i in range(n):
#     if (n%2==0):
#         counter +=1
# if(counter == 2):
#     print(f"The number {n} is a prime number")
# else:
#     print(f"The number {n} is not  a prime number")

# reverse a number
# num = int(input())
# n=num
# while n > 0:
#     last_number = n % 10
#     print(last_number,end="")
#     n = n // 10

# count the number
#  time complexity is O(1)

# num = int(input())
# count = 0
# while num > 0:
#     num = num // 10   #time complexity here is O(log(N)10)
#     count += 1
# print(count)

# palindrome number or string
 
# def number_palindrome(number):
#     num = number
#     palindrome_number = 0
#     while num>0:
#         last_digit  = num % 10
#         palindrome_number = (palindrome_number * 10) + last_digit
#         num = num // 10
#     if palindrome_number == number:
#         print(f"Entered number is a palindrome number :{palindrome_number}")
#     else:
#         print(f"Entered number is not a palindrome number :{palindrome_number}")

# def string_palindrome(string):
#     string1 = string
#     string_palindrome = string1[::-1]      
#     if string_palindrome == string1:
#         print(f"Entered string is a palindrome string :{string_palindrome}")
#     else:
#         print(f"Entered string is not a palindrome string :{string_palindrome}")

# user_input = input(f"Select what you want to check as a palindrome  1.number and 2.string \n")

# if(user_input == 'number'):
#     number = int(input())
#     number_palindrome(number)
# elif(user_input == 'string'):
#     string = input()
#     string_palindrome(string)
# else:
#     print("Opps!! Wait✋, You Have Entered A Wrong Option Try Again 👉👉")


#armstrong number

# n = int(input())
# user_input = n
# length = len(str(user_input))  
# sum = 0
# while user_input > 0:
#     individual_digit = user_input % 10
#     sum = sum + (individual_digit ** length)
#     user_input = user_input // 10   #time complexity here is O(log(N)10)
# if sum == n:
#     print(f"The number {n} is an armstrong number")
# else:
#     print(f"The number {n} is not an armstrong number")


#factors of a number
#Brute force approach  -- time complexity is O(n)
# n =int (input())
# num = n
# factors = []
# for i in range(1, (num+1)):
#     if num%i ==0:
#         factors.append(i)
# print(factors)

# Optimized approach -- time complexity is O(n//2) half
# n =int (input())
# num = n
# factors = []
# for i in range(1, (num//2)+1):
#     if num%i ==0:
#         factors.append(i)
# factors.append(n)
# print(factors)

#most efficient approach -- time complexity is O(sqrt(n))
# n = int(input())
# num = n
# factors = []
# for i in range(1, int((num**0.5))+1):
#     if num % i ==0:
#         factors.append(i)
#         if num//i !=i:
#             factors.append(num//i)
#     factors.sort()
# print(factors)


# Frequency Map / Dictionary time complexity is O(n)
# nums = [1, 2, 32, 432, 25, 6, 7, 8, 9]
# Frequency_Map = {}
# for i in range(0, len(nums)):
#     if nums[i] in Frequency_Map:
#         Frequency_Map[nums[i]] += 1
#     else:
#         Frequency_Map[nums[i]]=1
# print(Frequency_Map)

# Hashing
# n = [1, 2, 10, 4, 5, 8, 2, 1, 9, 6, 7, 8,1,2,4]
# m = [2,3,6,10,111,24,34,543,53,65,453,543,2,10,2,4,1,8,3,5]
# hash_map = [0] * 11
# for num in n:
#     hash_map[num] =+1
# for num in m:
#     if num<1 or num>10:
#         print(num,0)
#     else:
#         print(hash_map[num])
# print(hash_map)


n = [1, 2, 10, 4, 5, 8, 2, 1, 9, 6, 7, 8,1,2,4]
m = [2,3,6,10,111,24,34,543,53,65,453,543,2,10,2,4,1,8,3,5]
hash_map = {}
num = len(n)
for i in range(0,num):
    hash_map(num[i]) = hash_map.get(num[i],0)+1
print(hash_map)
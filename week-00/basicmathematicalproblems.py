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
 
def number_palindrome(number):
    num = number
    palindrome_number = 0
    while num>0:
        last_digit  = num % 10
        palindrome_number = (palindrome_number * 10) + last_digit
        num = num // 10
    if palindrome_number == number:
        print(f"Entered number is a palindrome number :{palindrome_number}")
    else:
        print(f"Entered number is not a palindrome number :{palindrome_number}")

def string_palindrome(string):
    string1 = string
    string_palindrome = string1[::-1]      
    if string_palindrome == string1:
        print(f"Entered string is a palindrome string :{string_palindrome}")
    else:
        print(f"Entered string is not a palindrome string :{string_palindrome}")

user_input = input(f"Select what you want to check as a palindrome  1.number and 2.string \n")

if(user_input == 'number'):
    number = int(input())
    number_palindrome(number)
elif(user_input == 'string'):
    string = input()
    string_palindrome(string)
else:
    print("Opps!! Wait✋, You Have Entered A Wrong Option Try Again 👉👉")

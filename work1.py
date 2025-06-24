# 1 . Write a function that takes a list of numbers and returns the maximum.
# def max():
#     list=[1,3,5,2,7,8]
#     a=0
#     for i in list:
#         if i>a:
#             a=i
#     print(a)        
# max()  
# 

# 2 . Define a function that returns the reverse of a given string.
# def reverse():
#     strg=input("enter the string:")
#     rev=""
#     for i in strg:
#         rev=i+rev
#     print(rev)
# reverse()        


# 3 . Write a function that takes a string and counts the number of vowels.
# def VOWELS():
#     str=input("Enter a character:")
#     count=0
#     for i in str:
#         if i in['a','i','o','e','u','A','E','I','O','U']:
#             count=count+1
#     print(count)
# VOWELS()

# 4 . Create a function to check if a number is a palindrome.

# def PALINDROME():
#     a=int(input("Enter a number: "))
#     original=a
#     rev=0
#     while a>0:
#         rev=rev*10 + a%10
#         a=a//10
#     if original==rev:
#         print("The number is a palindrome")
#     else:
#         print("It's not a palindrome")
# PALINDROME()        


# 5 . Define a function that accepts a list and returns a new list with only even numbers.
# def Even():
#     list1=[1,2,3,4,6,7,8,9] 
#     E_list=[]
#     for i in list1:
#         if(i%2==0):
#             E_list.append(i)
#     print(E_list)    
# Even()

# 
# 6 . Write a function that calculates the power of a number (without using ** or pow).

# def power(a,b):
#     result = 1
#     for i in range(b):
#         result *= a
#     print("power:", result)
# no1=int(input("Enter number:"))
# no2=int(input("Enter power:"))
# power(no1,no2)

# 7 . Create a menu-driven program using functions:
#  a) Add two numbers
#  b) Subtract two numbers
#  c) Multiply two numbers
#  d) Divide two numbers
#  e) Exit
#      (Use functions for each operation.)

# def add(a,b):
#     return a+b

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# def div(a,b):
#     if b!=0:
#         return a/b
#     else:
#         print("Cannot divide by zero")

# def menu():
#     while True:
#         print("\nMENU:")
#         print("1.ADD")
#         print("2.SUBTRACT")
#         print("3.MULTIPLY")
#         print("4.DIVIDE")
#         optn=int(input("Enter your choice :"))

#         a=int(input("Enter 1st number:"))
#         b=int(input("Enter 2nd number:"))

#         if  optn==1:
#             print("Result:",add(a,b))
#         elif  optn==2:
#             print("Result:",sub(a,b))
#         elif  optn==3:
#             print("Result:",mul(a,b))
#         elif  optn==4:
#             print("Result:",div(a,b))
#         else:
#             print("Enter a valid choice!")

# menu()     


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




#                       Recursive fn
#                 .......................  
# 
# 

# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x * factorial(x-1))
# num = 3
# print("The factorial of", num, "is", factorial(num))


# 1 . Write a recursive function to print numbers from n to 1.
# def print_num(no):
#     if no != 0:
#         print(no)
#         print_num(no-1)
# n1=int(input("Enter a number:"))
# print_num(n1)

#2 . Write a recursive function to calculate the sum of first n natural numbers.

# def s_no(n):
#     if n != 0:
#         return n + s_no(n - 1)
#     else:
#         return 0
# n1 = int(input("Enter a number: "))
# print("Sum:", s_no(n1))



# 3 . Write a recursive function to find the sum of digits of a number.
# def sum_digits(n):
#     if n==0:
#         return 0
#     else:
#         return (n % 10) + sum_digits(n // 10)
# n1=int(input("Enter a number: "))
# print("Sum of digits:", sum_digits(n1))

#4. Write a recursive function to reverse a string.

# def reverse(strg):

# def reverse(str):
#     if len(str)==0:
#         return str
#     return reverse(str[1:])+str[0]
# text=input("enter the text :")
# print("Reverse string:",reverse(text))






                         #   ANONYMOUS Fn
                     # .......................

# lambda_=lambda argument1,argument2:argument1+argument2
# print("value of the fn is :",lambda_(20,30))
# print("Value of the fn is :",lambda_(40,50))





#1 . Write a lambda function to find the square of a number.

# lambda_=lambda n1: n1**2
# a=int(input("Enter a number:"))
# print("The square is :",lambda_(a))


# 

# ....................
#2 . Write a lambda function to check if a number is even or odd.

# EVEN_NO= lambda n: "Even" if n % 2 == 0  else "Odd"
# a= int(input("Enter a number: "))
# print("The number is:",EVEN_NO(a))





# >>

#3 . Write a lambda function to find the maximum of two numbers

# max_num = lambda a, b: a if a > b else b
# n1 = int(input("Enter 1st number: "))
# n2 = int(input("Enter 2nd number: "))
# print("The greater number is:", max_num(n1,2))
# 






# 
#4 . Write a lambda function to check if a string starts with the letter 'A'

# letter_= lambda string: "True, bcz start with'A'" if string[0]=='A' or string[0]=='a' else "False"
# str= input("Enter a String: ")
# print("It is", letter_(str))        








# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.>

# string= input("Enter the string: ")
# a=len(string)

# if 1 <= a <= 10**5:
#     print("input string is",string)
#     for ch in range(a):
#         count=string.count(string[ch])
#         if count == 1:
#             print("First unique character:", string[ch])
#             print("index :",ch)
#             break
#     else:
#         print("-1")
# else:
#     print("Enter string of valid length")

       



a= [4,3,5,77,94]
b=[]

for i in a:
    if i > 0:
        b.append(i)

c = 1
while True:
    if c not in b:
        print("First missing positive:", c)
        break
    c += 1















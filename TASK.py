# task 3
# name=input("What is your name : ")
# age=int(input("How old are you : "))
# print(f"Hello {name}, You are {age} years old.")

# # task 4
# first= int(input("Enter first number: "))
# second= int(input("Enter second number: "))
# if first>second:
#     first+=10
# else:
#     first-=5
# print("Updated first number:", first)

# task 5
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# favorite=int(input("Enter your favorite number: "))
# print(f"Hello, {name}, You are {age} years old, and your favorite number is {favorite}.")


# # task  8,1
# i=int(input("enter the mark:"))
# if i<0 or i>100:
#     print("Enter a valid Mark")
# elif i>95 and i<=100:
#     print("You have 'O' grade With High Distinction")
# elif(i>=81):
#     print("You have A+ grade")    
# elif(i>=71):
#     print("You have A grade")    
# elif(i>=61):
#     print("You have B+ grade")
# elif(i>=51):
#     print("You have B grade")
# elif(i>=41):
#     print("You have C+ grade") 
# elif(i>=31):
#     print("You have C grade") 
# elif(i>=21):
#     print("You have D grade")                    
# else:
#     print("Failed")


#  task  8,2

# no=int(input("Enter a number: "))
# if no==0:
#     print("It is Zero")
# elif no>0:
#     print(no,"is Positive")
# else:
#     print(no,"is Negative")

# 9
# n=5
# for i in range(1,11):
#     for j in range(1,n+1):
#         a=i*j
#         print(f"{i}*{j}={i*j}", end="\t")
#     print()

# task 15
# Fav_food=['Biriyani','Porotta','Mandhi','Ice Cream','Shake']
# for i in Fav_food:
#     print(f'I Love eating {i}')

# tsak 16,1
# Squares= [i**2 for i in range(1, 11)]
# print("squares of no.s",Squares)

# 16,2
# txt='Python Programming is fun!'
# vowels=[char for char in txt if char in 'aeiouAEIOU']
# print(vowels)

# 16,3
# number=[i for i in range(1,21) if i % 2==0]
# print(number)


# # Password Validation Program

# password = ""

# # Keep asking until the correct password is entered
# while password != "python123":
#     password = input("Enter password: ")

# # Once correct password entered, else is executed
# else:
#     print("Correct password!")



#>>>>>...............................................tsk10
# pswd="python123"
# password= ""
# while password !=pswd:
#     password=input("Enter password : ")
# else:
#     print("Correct password.") 


# Find a Number in the List

# numbers=[1,2,3,4,5,6,7,8,9,10]
# target=3

# for i in numbers:
#     if i==target:
#         print("Number found!")
#         break
# else:
#     print("Number not found!")


# secret=24 
# guess=2  
# for i in range(guess):
#     a=int(input("Guess the secret number: "))
#     if a==secret:
#         print("Congratulations!....You guessed the correct number.")
#         break 
# else:
#     print("You failed to guess the number.") 



# >.........................................................................tsk 11
# Create a program to print a rectangle with 4 rows and 6 columns of stars.
# " Solution: for i in range(4): for j in range(6): print("*", end=" ") print()

# for i in range(4):        
#     for j in range(6):    
#         print("*", end=" ")
#     print()  

# 

# for i in range(5):
#     for j in range(5):
#         if i==0 or i==4 or j==0 or j==4:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()


# for i in range(5,0,-1):
#     for j in range(1, i + 1):
#         print(j,end=" ")
#     print()


# >................................................tks12
# def calculate_total(price,tax=5):
#     return price + (price*tax/100)
# print(calculate_total(100))



# items=["orange","cake"]
# def add_item(item):
#     global items  
#     items.append(item)
# add_item("apple")
# print(items)

# >>>>>>>>>>>>>>>......................................tsk 13

# Recursive function to reverse a string

# def reverse_string(str):
#     if len(str)==0: 
#         return str
#     else:
#         return reverse_string(str[1:]) + str[0] 
# print(reverse_string("hello world")) 
# 
# lambda_=lambda n1: n1**2
# a=int(input("Enter a number:"))
# print("The square is :",lambda_(a)) 




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.......................tsk17
# task 17/1: Extract the first and last character of a string
# a = "Programming"
# print(a[0], a[-1])  # Output: P g

# # task 17/2: Reverse a string
# a = "Programming"
# rev = a[::-1]
# print(rev)  # Output: gnimmargorP

# # task 17/3: Count occurrences of a specific character
# a = "Programming"
# print(a.count("m"))  # Output: 2

# # task 17/4: Replace spaces with underscores
# txt= "Python is fun to learn"
# print(txt.replace(" ", "_"))  # Output: Python_is_fun_to_learn

# # task 17/5: Check if a string is a palindrome
# txt="madam"
# print(txt==txt[::-1])  # Output: True



# >>>>>>>>...............................................tsk19


# weekdays=('Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday')
# print("First day: ",weekdays[0])
# print("Second day: ",weekdays[1])
# print("Slicing : ",weekdays[3:5])
# print("Index of Wednesday : ",weekdays.index('Wednesday'))

# Define two sets
s1={2,3,6,24,66,100,1,5}
s2={1,5,2,69,23,100}

# Union: all unique elements from both sets
print("Union:", s1 | s2)

# Intersection: common elements in both sets
print("Intersection:", s1 & s2)

# Difference: elements in s1 but not in s2
print("Difference (s1 - s2):", s1 - s2)

# Subset check: is s2 a subset of s1?
print("Is s1 > s2 (s2 subset of s1)?", s1 > s2) 
 # This checks if s2 is a subset of s1
print(s1>s2)
print(s1<s2)

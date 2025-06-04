# While loop
# 
# count = 1
# while count <= 5:
#     print(count)
#     count+=1
# else:
#     print("Loop completed successfully")
# # 
# 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>.............................................................................
#   



# 1 . Print numbers from 10 to 1
# Write a Python program using a while loop to print numbers from 10 down to 1.



# count=10
# while count >0:
#     print(count)
#     count=count-1 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.......................................................





# 2 . Sum of digits
# Write a program that takes a number as input and calculates the sum of its digits using a while loop.



# no=int(input("Enter a number: "))
# sum=0
# while no>0:
#     digit=no % 10      
#     sum +=digit     
#     no=no // 10        
# print("Sum of digits is:...",sum)


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>......................................



# 3 .  Check if a number is a palindrome
# Write a Python program using a while loop to check 
# if the entered number is a palindrome (same forwards and backwards)

# a=int(input("enter a no:"))
# while a>0:
#     if a==a[::-1]:
#         print("the no is palindrome")
#     else:
#         print("its not a palindrome")


# a=int(input("Enter a number: "))
# original=a
# rev=0
# while a>0:
#     rev=rev*10 + a%10
#     a=a//10
# if original==rev:
#     print("The number is a palindrome")
# else:
#     print("It's not a palindrome")



# >>>>>>>>>>>>..................................................................

# 4 .Count the number of digits Input a number and
#  count how many digits it has using a while loop



# num=int(input("Enter a number: "))  
# count=0
# if num==0:
#     count=1
# else:
#     num=abs(num)
#     while num>0:
#         num=num // 10
#         count+=1
# print("Number of digits:",count)




# >>>>>>>>>>>>>>>...........................................................................





# 5 . Keep asking input until user enters ‘quit’Write a program
#  that keeps asking the user to enter a word, and stops only when they type 'quit'.


# a=""
# while a.lower()!= "quit":
#     a=input("Enter the word:")






# 6 . Count how many times a digit appears Input a number and a digit,
# then count how many times that digit appears in the number using a while loop.


# num=int(input("Enter the number :"))
# digit=int(input("Enter the digit to count:"))
# count=0
# while num>0: 
#     d=num%10
#     if d==digit:
#         count+=1
#     num=num//10       
# print(count,"times the digit appears")






# num=input("Enter a number:")
# digit=input("Enter a digit to count:")
# i=0
# count=0
# while i<len(num):
#     if num[i]==digit:
#         count+=1
#     i=i+1
# print(count,"times the digit appears")








# Check for Armstrong number Input a number and use a while loop to check 
# if it’s an Armstrong number (e.g., 153 → 1³ + 5³ + 3³ = 153).



# num= int(input("Enter a number: "))
# original=num  
# sum = 0
# while num > 0:
#     digit = num % 10        
#     sum += digit ** 3       
#     num = num // 10         
# if sum == original:
#     print(original, "is an Armstrong number.")
# else:
#     print(original, "is not an Armstrong number.")






# a=""
# b=0
# while a9!= -1:
#     a=int(input("Enter the no:"))
#     if a!=-1:
#         b=b+a
# print(b)  
# 
# 
# a=int(input("enter a number:"))
# b=0
# while a!=-1:
#     b=b+a
#     a=int(input("enter a no:")) 
# print(b)        


   






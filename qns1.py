# 1.Find the sum of all even numbers between 1 and N

# a=int(input("enter the no:"))
# sum=0
# for i in range(a+1):
#     if(i%2==0):
#         sum=sum+i
# print("sum of the even no.s :",sum) 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.............


# 2.Count vowels in a string

# str=input("Enter a character:")
# count=0
# for i in str:
#     if i in['a','i','o','e','u','A','E','I','O','U']:
#         count=count+1
# print(count)        

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..............


# 3.Find the maximum number in a list Given a list of numbers, use a for loop to find the maximum number.
   
# lst1=[183,605,421,1782,900]
# maximum=0
# for i in lst1:
#     if i>maximum:
#         maximum=i
# print("maximum no in the list:",maximum)  

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....................................


# 4.Calculate the product of all numbers in a listGiven a list of numbers,
# write a program to calculate the product (multiplication) of all the numbers using a for loop.

# numbers=[2,3,4,5,6]
# product=1
# for i in numbers:
#     product=product*i
# print("The product of all numbers is:", product)




# a=int(input("enter the no:"))
# b=0
# for i in str(a):
#      b+=int(i)
# print(b)        

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.....................................




# 5. Reverse a string using a for loop Input a string and print its reverse using a for loop

# strg=input("enter the string:")
# rev=""
# for i in strg:
#     rev=i+rev
# print(rev)    

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>................................





# 6.Print characters at even indices Input a string and 
# use a for loop to print characters at even positions (index 0, 2, 4, …).

# str=input("Enter a character:")
# b=""
# for i in range(0,len(str),2):
#     b=b+' '+(str[i])
# print(b)



# 
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>..........................................................





#   7 . Find common elements in two lists Input two lists and use a for loop to print elements present in both.

list1 =(input("Enter elements of first list: "))
list2 =(input("Enter elements of second list: "))
common=[]
for i in list1:
    if i in list2:
        common.append(i)
print("Common elements are:",common)



#  list comprehension ,(throwaway variable)
# list1=[input() for a in range(int(input("Enter number of elements of 1st list: ")))] 
# list2=[input() for a in range(int(input("Enter number of elements of 2nd list: ")))]
# print("First list:",list1)
# print("Second list:",list2)
# common=[]
# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)
# print("Common elements are:",common)
  




# a=int(input("Enter the number: "))
# b=len(str(a))
# sum=0
# for i in range(0,b):                                 
#     d=a%10
#     sum=sum+d
#     a=a//10    
# print("Sum is:",sum)
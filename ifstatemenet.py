# if statement

# i=10
# if(i>9):
#     print("10 is less than 15")
# print("iam not in if")


# ......................................................

# if else 

# i=20
# if(i<15):
#     print("i is smaller than 15")
#     print ("iam in if block")
# else:
#     print("i is greater than 15")
#     print("iam in else block")
# print("iam not in if and not in else Block")     

# .......................................................


# nested if

# i=10
# if(i==10):
#     if(i<15):
#         print("i is smaller than 15")
#     if(i<12):
#         print("i is smaller than 12 too")
#     else:
#         print("i is greater than 15")        

# ........................................................


# if elif else

# i=20
# if(i==10):
#     print("i is 10")
# elif(i==15):
#     print("i is 15")
# elif(i==20):
#     print("i is 20") 
# else:
#     print("i is not present")            

#....................................................... 





a=int(input("enter the no:"))
if(a%2==0):
    print(" the no is even")
else:
    print("the no is odd")    


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.



i=int(input("enter the no:"))
if(i<0):
    print("the no is -ve")
elif(i>0):
    print("the no is +ve") 
else:
    print("the no is zero")    



str=input("Enter a character:")
if str in['a','i','o','e','u','A','E','I','O','U']:
    print("is a vowel")
else:
    print("its not a vowels")    





       

i=int(input("enter the mark:"))
if (i<0 or i>100):
    print("enter a valid mark")
elif(91<=i<=100):
    print("O grade")
elif(i>=81):
    print("A+ grade")    
elif(i>=71):
    print("A grade")    
elif(i>=61):
    print("B+ grade")
elif(i>=51):
    print("B grade")
elif(i>=41):
    print("C+ grade") 
elif(i>=31):
    print("C grade") 
elif(i>=21):
    print("D grade")                    
else:
    print("Failed")



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


print("1.Addition\n","2.Subtraction\n","3.Division\n","4.Multiplication")
oprtn=int(input("choose a operation..."))

if(oprtn==1):
    a=int(input("Enter the first no:"))
    b=int(input("Enter the second no:"))
    sum=a+b
    print(sum)
elif(oprtn==2):
    a=int(input("Enter the first no:"))
    b=int(input("Enter the second no:"))
    sub=a-b
    print(sub)
elif(oprtn==3):
    a=int(input("Enter the first no:"))
    b=int(input("Enter the second no:"))
    if(b>0):
        div=a/b
        print(div)
    else:
        print("secnd no. can not be 0")    
elif(oprtn==4):
    a=int(input("Enter the first no:"))
    b=int(input("Enter the second no:"))
    mul=a*b
    print(mul)
else:
    print("enter a valid option")            
    
    









       

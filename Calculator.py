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
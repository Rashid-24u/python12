print("ENTER 3 NUMBERS")
x=int(input("enter first number:"))
y=int(input("enter second number:"))
z=int(input("enter third number:"))
if(x==y and y==z and x==z):
    print("three no.s are same")
elif(x>y and x>z):
    print(x,"is the greatest number")
elif(y>x and y>z):
    print(y,"is the greatest number")  
else:
    print(z,"is the greatest number")      
# 
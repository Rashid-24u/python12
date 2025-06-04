i=int(input("enter the mark:"))
if i<0 or i>100:
    print("Enter a valid Mark")
elif i>95 and i<=100:
    print("You have 'O' grade With High Distinction")
elif(i>=81):
    print("You have A+ grade")    
elif(i>=71):
    print("You have A grade")    
elif(i>=61):
    print("You have B+ grade")
elif(i>=51):
    print("You have B grade")
elif(i>=41):
    print("You have C+ grade") 
elif(i>=31):
    print("You have C grade") 
elif(i>=21):
    print("You have D grade")                    
else:
    print("Failed")
#                       EXCEPTIONS
#                    ................
# # Type error
# x=5
# y="hello"
# z=x+y 
# Raise a type Error:unsupported operand type(s) for +:'int' and 'str'


# Try catch block to resolve it:

# x=5
# y="hello"
# try:
#     z=x+y
# except TypeError:
#     print("Error:cannot add an int and str")  


# a=[1,2,3]
# try:
#     print("2nd element=",a[1])
#     print("4th element=",a[3])
# except:
#     print("an error occured")   

# a=[1,2,3]
# try:
#     print("2nd element=",a[1])
#     print("4th element=",a[3])
# except Exception as e:
#     print(e)    


# Raisning Exception
# program to depict Raising exception

# try:
#     raise NameError("hi there")   #raise error
# except NameError:
#     print("An exception")
#     raise     #To dtermine whether the Exception was raised or not as
# 
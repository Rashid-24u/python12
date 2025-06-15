#                                              Fn Arguments
#                                        ..........................

#   1. Default arguments

# def fn(n1,n2=20):
#     print("number 1 is  :",n1)
#     print("number 2 is  :",n2)
# print("passing only one argument")
# fn(30)

#     2. Keyword arguments

# def fn(n1,n2):
#     print("number 1 is  :",n1)
#     print("number 2 is  :",n2)
# print("withou using keywordt")
# # fn(2,3)
# fn(n2=10,n1=20)



# .................................................................................................................................

                                                #   ANONYMOUS Fn
                                            # .......................


# 
# lambda_=lambda argument1,argument2:argument1+argument2
# print("value of the fn is :",lambda_(20,30))
# print("Value of the fn is :",lambda_(40,50))



# .................................................................................................................................



#                      python fn within another fn
#                  ..................................

# 
# def word():
#     string='python fn tutorials'
#     x=5
#     def number():
#         print(string)
#         print(x)
#     number()
# word()        




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





          
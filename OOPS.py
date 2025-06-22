# class Employee:
#     id=10
#     name="Rashid"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# emp.display()        

    # delete cheyyenenkil-->
# class Employee:
#     id=10
#     name="Rashid"
#     def display(self):
#         print("ID:%d\nName:%s"%(self.id,self.name))
# emp=Employee()
# del emp.id
# del emp.name
# emp.display()



#...OBGECT

# class Car:
#     def __init__(self,modelname,year):
#         self.modelname=modelname
#         self.year=year
#     def display(self):
#         print(self.modelname,self.year) 
# c1=Car("Toyota",2016)
# c1.display()           


# non parameter constructor

# class Student:
#     def __init__(self):
#         print("This is non parameterized condtructor")
#     def show(self,name):
#         print("Hello",name)
# student=Student()
# student.show("john")


# Default constructor

# class Student:
#     roll_num=101
#     name="Momi"

#     def display(self):
#         print(self.roll_num,self.name)

# st=Student()        
# st.display()





#####################
#####################


# class Student:
#     def __init__(self,name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age

# # create the object of the class Student
# s=Student("John",101,22)      
# # prints the attribute name of the objects s
# print(getattr(s,'name')) 


# #reset  the value of attribute age to 23
# setattr(s,"age",23)
# # print the modified value of age
# print(getattr(s,'age'))
        

# ##print true if the student contains the attribute with the name id
# print(hasattr(s,'id'))   
# ## deletes the attribute age
# delattr(s,'age')

# ## this will give an error since the attribute age has been deleted
# print(s.age)






##??????????????????????????????????????????????????????????????????????????????????????????????????????????????????????
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


#Homework

#1 . Create a class Student with attributes name, roll_number, and marks.Add a method to display student details.

# class Student:
#     name="sulu"
#     roll_number=101
#     mark=90

#     def displayDetails(self):
#         print("Name:",self.name , "Roll no:",self.roll_number , "Mark:",self.mark)
# st=Student()
# st.displayDetails()

#2 . Create a class Rectangle with attributes length and width.Add a method to calculate and display the area.

# class Rectangle:
#     def __init__(self,length,width):
#         self.length = length
#         self.width = width

#     def Calculate_Area(self):
#         area= self.length * self.width
#         print("Area of the rectangle :",area)

# rectangle=Rectangle(20,10)
# rectangle.Calculate_Area()

#3 . Create a class Car with attributes brand, model, and year.Add a method to display full details of the car.

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand=brand
#         self.model=model
#         self.year=year
#     def displayDetails(self):
#         print("Brand:",self.brand ,"Model Name:",self.model ,"Year:",self.year)
# c1=Car("Benz","SUV",2021)
# c1.displayDetails()

#4 . Create a class Person with attributes name and age.Add a method to check if the person is eligible to vote (age ≥ 18).

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def check_eligibility(self):
#         if self.age>=18:
#             print(self.name,"is eligible to vote.")
#         else:
#             print(self.name,"is not eligible to vote.")

# p1=Person("momi",17)
# p1.check_eligibility()

# p2=Person("sulu",20)
# p2.check_eligibility()

#5 . Create a class BankAccount with attributes account_holder and balance.Add methods to deposit, withdraw, and check balance.

# class Bank_Acc:
#     def __init__(self,account_holder,balance):
#         self.account_holder=account_holder
#         self.balance=balance
#         print("Account holder:",self.account_holder) 
    
#     def deposit(self,amount):
#         self.balance +=amount 
#         print(amount,"deposited.  " "  New balance:",self.balance) 

#     def withdraw(self,amount):
#         if amount>self.balance:
#             print("Insufficient balance.")
#         else:
#             self.balance -= amount
#             print(amount, "withdrawn.  New balance:", self.balance)    

#     def check_balance(self):
#         print("Current balance:",self.balance) 

# b1=Bank_Acc("Rashid",0)      
# b1.deposit(500)
# b1.withdraw(200) 
# b1.check_balance()     




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        print("Account created for:", self.account_holder)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")


name= input("Enter account holder name: ")
account= BankAccount(name)

while True:
    print("\n--- Bank Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice= input("Enter your choice (1-4): ")

    if choice== "1":
        amt =int(input("Enter amount to deposit: "))
        account.deposit(amt)
    elif choice== "2":
        amt=int(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice== "3":
        account.check_balance()
    elif choice== "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice.")

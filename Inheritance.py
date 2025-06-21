#   >>>  >>>>  >>>>  SINGLE INGERITANCE

# class Animal:
#     def speak(self):
#         print("Animal speacking")
## ....child class Dog inherits the base class Animal
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# d=Dog()
# d.bark()
# d.speak()  



#   >>>  >>> >>> >>> MULTI-LEVEL INHERTANCE

# class Animal:
#     def speak(self):
#         print("Animal speacking")
# # .... the child class Dog inherits the base class Animal
# class Dog(Animal):
#     def bark(self):
#         print("dog barking")
# #..... the child class Dog child inherits another child class Dog
# class DogChild(Dog):
#     def eat(self):
#         print("Eating bread..")

# d=DogChild()
# d.bark()
# d.speak()
# d.eat()



#  >>>  >>>  >>>  MULTIPLE  INHERITANCE

# class Calculation1:
#     def Summation(self,a,b):
#         return a+b
# class Calculation2:
#     def Multiplication(self,a,b):
#         return a*b  
# class Derived(Calculation1,Calculation2):
#     def Derived(self,a,b):
#         return a/b

# d=Derived()
# print(d.Summation(10,20))
# print(d.Multiplication(10,20)) 
# print(d.Derived(10,20))        



# >> >>> >>>  HIERACHICAL INHERITANCE

# # Base class
# class Parent:
#     def fn1(self):
#         print("this fn is in parent class.")

# # Derived class 1
# class Child1(Parent):
#     def fn2(self):
#         print("This function is in child 1")

# # Derived class 2
# class Child2(Parent):
#     def fn3(self):
#         print("This function is in child 2")
# a=Child1()
# a.fn1()
# a.fn2()

# b=Child2()
# b.fn1()
# b.fn3()




# >> >>> >>>  HYBRID INHERITANCE

# Base class
class Vehicle:
    def display(self):
        print("This is a Vehicle.")
class Bike(Vehicle):
    def show_bike(self):
        print("This is a Bike.")
class Car(Vehicle):
    def show_car(self):
        print("This is a car")
class Road(Bike,Car):
    def move(self):
        print("The vehicles are moving on the road.")
i=Road()

i.display()         
i.show_bike()    
i.show_car()   
i.move()     

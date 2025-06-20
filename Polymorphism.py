# class Animal:
#     def speak(self):
#         print("speaking")
# class Dog(Animal):
#     def speak(self):
#         print("Barking")

# d=Dog()
# d.speak() 






# class Bank:
#     def getroi(self):
#         return 10;
# class SBI(Bank):
#     def getroi(self):
#         return 7;
# class ICICI(Bank):
#     def getroi(self):
#         return 8;
# b1=Bank()
# b2=SBI()
# b3=ICICI()

# print("Bank rate of interest:",b1.getroi())
# print("SBI rate of interest:",b2.getroi())
# print("ICICI rate of interest:",b3.getroi())





class Bird:
    def intro(self):
        print("there are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot")

class sparrow(Bird):
    def flight(self):
        print("Sparrow can fly")

class ostrich(Bird):
    def flight(self):
        print("ostrich cannot fly")        
a=Bird()
b=sparrow()
c=ostrich()

a.intro()
a.flight()
b.intro()
b.flight()
c.intro()
c.flight()


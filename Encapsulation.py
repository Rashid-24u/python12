# class Base: 
# 	def __init__(self): 
# 		# Protected member 
# 		self._a = 2
# # Creating a derived class 
# class Derived(Base): 
# 	def __init__(self): 
# 		# Calling constructor of 
# 		# Base class 
# 		Base.__init__(self) 
# 		print("Calling protected member of base class: ", self._a) 
# 		# Modify the protected variable: 
# 		self._a = 3
# 		print("Calling modified protected member outside class: ", self._a) 
# obj1 = Derived() 

# obj2 = Base() 

# # Calling protected member 
# # Can be accessed but should not be done due to convention 
# print("Accessing protected member of obj1: ", obj1._a) 

# # Accessing the protected variable outside 
# print("Accessing protected member of obj2: ", obj2._a) 





#............................PRIVATE MEMBERS


class Base: 
      def __init__(self): 
        self.a = "Hello"
        self.__c = "World"

# Creating a derived class 
class Derived(Base): 
    def __init__(self): 

        # Calling constructor of 
        # Base class 
        Base.__init__(self) 
        print("Calling private member of base class: ") 
        print(self.__c) 
obj1 = Base() 
print(obj1.a) 
obj2=Derived()

# Uncommenting print(obj1.c) will 
# raise an AttributeError 

# Uncommenting obj2 = Derived() will 
# also raise an AttributeError as 
# private member of base class 
# is called inside derived class 





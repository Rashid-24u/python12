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


class Student:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age

# create the object of the class Student
s=Student("John",101,22)      
# prints the attribute name of the objects s
print(getattr(s,'name')) 


#reset  the value of attribute age to 23
setattr(s,"age",23)
# print the modified value of age
print(getattr(s,'age'))
        

##print true if the student contains the attribute with the name id
print(hasattr(s,'id'))   
## deletes the attribute age
delattr(s,'age')

## this will give an error since the attribute age has been deleted
print(s.age)
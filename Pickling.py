# import pickle
# #Data to be picked

# students=[{"name":"Alice","age":20},{"name":"Bob","age":22}]
# #writing to a file

# with open("students.pkl","wb") as file:
#     pickle.dump(students,file)


import pickle
with open("students.pkl","rb")as file:
    loaded_students=pickle.load(file)
    print(loaded_students)
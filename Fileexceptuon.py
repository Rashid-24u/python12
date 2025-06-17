# f=open('file123.py','x')                  # file creating

# file=open('file123.py','r')               #read full
# for each in file:
#     print(each)

# f=open('file123.py','r')
# print(f.readline())                       # read one line
# print(f.readline())
# f.close()

# file=open('file123.py','r')
# print(file.read())                        # full read another way


# with open("file123.py") as file:
#     data=file.read()                      # full read another way
#     print(data) 


# file=open('file123.py','r')
# print(file.read(5))                       #read character wise



# with open("file123.py") as file:
#     data=file.readlines()
#     for line in data:
#         word=line.split()               
#         print(word)





#                        ......................Write().....................
# ...........................................................................................................................


# file=open('file123.py','w')
# file.write("This is write commaand")
# file.write("It allows us to write in aparticular file")       # munne kodutha file le content change aayi ,, ith vannu
# file.close()


# file=open('file123.py','w')
# file.write("hi")
# file.write(" rashid")      
# file.close()

file=open('file123.py','a')
file.write("\nthis will add this line")      
file.close()
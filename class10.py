
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....Square
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         print("* ",end=" ")
#     print()    




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...Right half

n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("* ",end="")
    print()  
# # 



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..Inverted Righthalf

# n=5
# for i in range(0,n):
#     for j in range(i,n):
#         print("* ",end=" ")
#     print()   



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....Left Half
n=5
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end="")
    for k in range(0,i+1):
        print("*",end="")
    print() 



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>...FULL PYRAMID

# n=5
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print("* ",end="")
#     print() 



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..............INverted Fullpyramid

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n-i):
#         print("* ",end="")
#     print() 



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>................inverted left half

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n-i):
#         print("*",end="")
#     print()
# 



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>........................RHOMBUS

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n):
#         print("*",end="")
#     print()        




# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>................FLOYDS
# n=5
# a=1
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(a,end=" ")
#         a+=1
#     print()    



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>................DIAMOND

# n=6
# a=4
# for i in range(0,a):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print("* ",end="")
#     print()    
# for l in range(0,a-1):
#     for m in range(0,a+l):
#         print(" ",end="")
#     for p in range(1,a-l):
#         print("* ",end="") 
#     print()           


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>................Hourglass

# n=4
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n-i):
#         print("* ",end="")
#     print()    
# for a in range(0,n-1):
#     for b in range(0,n-1-a):
#         print(" ",end="")
#     for c in range(0,a+2):
#         print("* ",end="")
#     print()   



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..................... Pascals triangle

# n=4
# for i in range(0,n):
#     for j in range(0,n-i):
#         print(" ",end="")
#     for k in range(0,i+1):
#         print("1 ",end="")
#     print()











# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..................Hollow sqare

# n=5 
# for i in range(n):
#     for j in range(n):
#         if i==0 or i==n-1 or j==0 or j==n-1:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..............Hollow full pyramid

    
# n=4
# for i in range(0,n):
#     for j in range(0,n-i):
#            print(" ",end="")
#     for k in range(0,i+1):
#         if(i==n-1):
#            print("* ",end="")  
#         elif k==0 or k==i:
#             print("* ",end="")
#         else:
#              print(" ",end=" ")    
                
#     print() 

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>............Hollow inverted full pyramid

# n=5
# for i in range(0,n):
#     for j in range(0,i+1):
#         print(" ",end="")
#     for k in range(0,n-i):
#         if i==0 or k==0 or k==n-i-1:
#           print("* ",end="")
#         else:
#              print(" ",end=" ")   
#     print() 


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>..................Hollow DIAMOND pyramid
n=4
for i in range(0,n):
    for j in range(0,n-i):
           print(" ",end="")
    for k in range(0,i+1):  
        if k==0 or k==i:
            print("* ",end="")
        else:
             print(" ",end=" ")    
    print()  
for a in range(0,n-1):
    for j in range(0,a+2):
        print(" ",end="")
    for k in range(0,n-a-1):
        if k==0 or k==n-a-2:
          print("* ",end="")
        else:
             print(" ",end=" ")   
    print()  


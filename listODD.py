list=[1,2,3,4,5,6,7,8,9,10]
list2=[]
list3=[]
b2=0
c2=0
for i in  list:
    if(i%2==0):
        list2.append(i)
        b2=b2+i
    else:
        list3.append(i)
        c2=c2+i    
print(list2)
print(list3)  
print("sum of list2:",b2)
print("sum of list3:",c2)      





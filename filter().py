# X>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   Filters in an iterable based on a condition

nums=[1,2,3,4,5]
even=list(filter(lambda x:x %2==0,nums))
print(even)
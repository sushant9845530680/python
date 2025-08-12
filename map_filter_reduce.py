#  map___________________________
# number=[1,4,39,39,22,2]

# def square(x):
#     return x*x

# y= map(square,number)     #new= map(lamda x: x*x, number)
# print(list(y))


#filter____________
# number=[10,2,3,30,443,32,44,22]

# def greater(x):
#     if x>9:
#         return True
#     else:
#         return False
    
# new=filter(greater,number)
# print(list(new))


from functools import reduce
number=[1,2,3,4,5,6]
        # [3,3,4,5,6]
        # [6,4,5,6]
        # [10,5,6]
        # [15,6]
        # [21]
def fun(a,b):
    return a+b
c= reduce(fun,number)
print(c)
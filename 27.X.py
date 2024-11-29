'''issubclass(sub,sup)---sub,superclass check the rightside super class of left side'''
# class Calulation1:
#         def summation(self,a,b):
#                 return a+b;
# class Calulation2:
#         def multipication(self,a,b):
#                 return a*b;
# class Derived(Calulation1,Calulation2):
#         def divide(self,a,b):
#                 return a/b;

# d=Derived()
# print(issubclass(Derived,Calulation2))
# print(issubclass(Calulation1,Calulation2))

             # True
             # False

'''isinstance(obj,class)---check the object and classes'''
# class Calulation1:
#         def summation(self,a,b):
#                 return a+b;
# class Calulation2:
#         def multipication(self,a,b):
#                 return a*b;
# class Derived(Calulation1,Calulation2):
#         def divide(self,a,b):
#                 return a/b;

# d=Derived()
# print(isinstance(d,Derived))
# print(isinstance(Calulation1,Calulation2))

#             True
#             False
'''Iterators---countable no. of value---not use of for'''
# num=[1,2,3,4,5,6]
# obj=iter(num)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

#            1
#            2
#            3
#            4
#            5
#            6

'''iter through  string'''
# mystr='banana'
# myit=iter(mystr)
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))

             # b
             # a
             # n
             # a
             # n
             # a
''' "yield --looping"'''
# def nums():
#         for i in range(1,5):
#                 yield i
# obj=nums()
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))

        # 1
        # 2
        # 3
        # 4
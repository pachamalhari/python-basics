# What is Abstraction in Python?

'''Basically, Abstraction focuses on hiding the internal implementations of a process or method from the user.
In this way,the user knows what he is doing but not how the work is being done.'''


# Abstract Classes and Methods in Python


'''To declare an Abstract class, we firstly need to import the abc module.'''

# from abc import ABC
# class abs_class(ABC):
#      #abstract methods
#      pass

'''As a property, abstract classes can have any number of abstract
methods coexisting with any number of other methods. For example we can see below.'''

# from abc import ABC, abstractmethod
# class abs_class(ABC):
#     #normal method
#     def method(self):
#         #method definition
#         pass
#     @abstractmethod
#     def Abs_method(self):
#         #Abs_method definition
#         pass

'''Here, method() is normal method whereas Abs_method() 
    is an abstract method implementing @abstractmethod from the abc module.'''


from abc import ABC, abstractmethod
class Absclass(ABC):
    def printTxt(self,x):
        print("Passed value: ", x)
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")
 
class test_class(Absclass):
    def task1(self):
        print("We are inside test_class task")
 
class example_class(Absclass):
    def task(self):
        print("We are inside example_class task")
 
#object of test_class created
# test_obj = test_class()
# test_obj.task()
# test_obj.printTxt(100)
 
#object of example_class created
example_obj = example_class()
example_obj.task1()
example_obj.printTxt(200)

# print("test_obj is instance of Absclass? ", isinstance(test_obj, Absclass))
print("example_obj is instance of Absclass? ", isinstance(example_obj, Absclass))

'''Abseration---no content in function @---decorator to importABC hide the methods'''
'''abc inheritance and atleast one abserat method (using dector)'''
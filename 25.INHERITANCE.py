'''single Inheritance'''
# class Animal:
#         def speak(self):
#                 print('Animal Speaking')
# class Dog(Animal):
#         def bark(self):
#                 print('dog barking')
# d=Dog()
# d.bark()
# d.speak()

         #dog barking
         #Animal Speaking

'''Question---user iput,lower,[0],len'''
# class Hari:
#         def __init__(self):
#          c=input('ENTER THE STRING :')
#          self.c=c
#         def input_user(self):
#                 print(self.c.lower())
#                 print(self.c[0])
# class student(Hari):
#         def length(self):
#                 print(len(self.c))

        
# d=student()
# d.input_user()
# d.length()

                      #harikaran
                      #H
                      #9

'''Multi-level inheritance'''
# class Animal:
#         def speak(self):
#                 print('Animal Speaking')
# class Dog(Animal):
#         def bark(self):
#                 print('dog barking')
# class DogChild(Dog):
#         def eat(self):
#                 print('Eating bread..')
# d=DogChild()
# d.bark()
# d.speak()
# d.eat()

               # dog barking
               # Animal Speaking
               # Eating bread..

'''"disturbiting" '''
# class Hari:
#         def __init__(self):
#          c=input('ENTER THE STRING :')
#          self.c=c
#         def input_user(self):
#                 print(self.c.lower())
#                 print(self.c[0])
# class student(Hari):
#         def length(self):
#                 print(len(self.c))
# class vowels(student):
#        def extract(self):
#               for i in self.c:
#                 if i in 'aeiouAEIOU':
#                       li=''
#                       print(li+i,end='')

        
# d=vowels()
# d.input_user()
# d.length()
# d.extract()

               #aeerjttwdfg
               #a
               #11
               #aee

'''Multiple inheritance   "grouping " multiple parent '''
# class Calulation1:
#         def summation(self,a,b):
#                 return a+b;
# class Calulation2:
#         def multipication(self,a,b):
#                 return a*b;
# class Calulation3(Calulation1,Calulation2):
#         def divide(self,a,b):
#                 return a/b;

# d=Calulation3()
# print(d.summation(10,20))
# print(d.multipication(10,20))
# print(d.divide(10,20))

              # 30
              # 200
              # 0.5

'''Hierarchical Inheritance ---multiple child'''
# class Parent:
#         def function1(self):
#                 print('This is in parent class.')
# class Child1(Parent):
#         def function2(self):
#                 print('This function is in child 1.')
# class Child2(Parent):
#         def function3(self):
#                 print('This function is in child 2.')

# object1=Child1()
# object2=Child2()
# object1.function1()
# object1.function2()
# object2.function1()
# object2.function3()

               # This is in parent class.
               # This function is in child 1.
               # This is in parent class.
               # This function is in child 2.

'''Hybrid inheritance---- all type of inheritance'''
# class School:
#         def function1(self):
#                 print('This function is in school.')
# class Student1(School):
#         def function2(self):
#                 print('This function is in student 1.')
# class Student2(School):
#         def function3(self):
#                 print('This function is in student 2.')
# class Student3(Student1,School):
#         def function4(self):
#                 print('This function is in student 3.')

# object=Student3()
# object.function1()
# object.function2()

                # This function is in school.
                # This function is in student 1.

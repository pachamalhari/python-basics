'''Python Object'''
# class myclass:
#     x=5
# p1= myclass()
# print(p1.x)
# print(type(p1))

        #5
        #  <class '__main__.myclass'>

'''greet "self--current instance/object of the class" create a function inside a def'''
# class mygreet:
#     def greet(self):
#         print('hello World')

# p1=mygreet()
# p1.greet()


             # hello World #

'''add by using self'''
# class addition:
#     def add(self,a,b):
#         print(a+b)

# p1=addition()
# p1.add(10,20)

        ## a ##


'''__init__() '''
# class operation:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print(self.a+self.b)

#     def subs(self):
#         print(self.a-self.b)
    
#     def mulp(self):
#         print(self.a*self.b)

#     def div(self):
#         print(self.a/self.b)
        


# p1=operation(10,20)
# p1.add()
# p1.subs()
# p1.mulp()
# p1.div()
             # 30
             # -10
             # 200
             # 0.5  




'''Encapsulation----wrapping data'''
# class India():
#         def capital(self):
#                 print('New Delhi is the capital of india')
#         def language(self):
#                 print('Hindi is the most widely spoken language of india')
#         def type(self):
#                 print('India is a developing country')
# class USA():
#         def capital(self):
#                 print('Washington is the capital of USA')
#         def language(self):
#                 print('English is the primary language of USA')
#         def type(self):
#                 print('USA is a developed country')  

# obj_ind=India()
# obj_usa=USA()
# for country in (obj_ind,obj_usa):
#         country.capital()
#         country.language()
#         country.type()

           # New Delhi is the capital of india
           # Hindi is the most widely spoken language of india
           # India is a developing country
           # Washington is the capital of USA
           # English is the primary language of USA
           # USA is a developed country








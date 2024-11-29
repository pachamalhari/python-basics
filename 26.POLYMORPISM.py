'''polymorphism----Method Overriding in inheritance---child override parent function'''
# class Animal:
#         def speak(self):
#                 print('speaking')
# class Dog(Animal):
#         def speak(self):
#                 print('barking')

# d=Dog()
# d.speak()

#                  barking


'''super() to get overriding function'''
# class Animal:
#        def speak(self):
#                 print('speaking')
# class Dog(Animal):
#         def speak(self):
#                 print('barking')
#                 super().speak()

# d=Dog()
# d.speak()

               # barking
               # speaking

'''Rate of interest'''
# class Bank:
#         def getroi(self):
#                 return 10;
# class SBI(Bank):
#         def getroi(self):
#                 return 7;
# class ICICI(Bank):
#         def getroi(self):
#                 return 8;
# b1=Bank()
# b2=SBI()
# b3=ICICI()
# print('Bank Rate of interest :',b1.getroi())
# print('SBI Rate of interest :',b2.getroi())
# print('ICICI Rate of interest :',b3.getroi())

              # Bank Rate of interest : 10
              # SBI Rate of interest : 7
              # ICICI Rate of interest : 8

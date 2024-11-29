''' GREETINGS '''
# def greet():
#     print('Hello World!')

# greet()

            ##  Hello World!  ##


''' BASIC ADDITION '''
# def add(x,y):
#     sum=x+y
#     print('Sum:',sum)

    
# add(5,5)
         
         ##10##


''' ARGUMENTS '''
# def arg():
#     name=input('ENTER THE NAME : ')
#     print('hello '+name)


# arg()

                  ##ENTER THE NAME : HARI
                  ##hello HARI


''' CHANGE ALL CAPS INTO LOWER '''
# def lower():
#     a=input('ENTER THE STRING : ')
#     print(a.lower())


# lower()

               ##ENTER THE STRING : HAriKaRan
               ##harikaran


''' ADDING NUMBERS WITH ONE,TWO, NO SUGGESTIONS '''
# def add(x=200,y=100):
#     sum=x+y
#     print('sum :',sum)


# add(5)
# add(5,5)
# add()

             ## sum : 105 ##
             ## sum : 10  ##
             ## sum : 300 ##


''' ADDING NUMBERS USING "def & return" '''
# def addNum(a,b):
#     sum=a+b
#     mul=a*b
#     return f"sum={sum},mul={mul}"
    
   

# print(addNum(1,2))
# print('function ended')

           ###       sum=3,mul=2
           ###       function ended  

''' Method 2 '''
# def addNum(a,b):
#     sum=a+b
#     mul=a*b
#     return f"sum={sum},multiply={mul}"
    
   

# fun=addNum(10,5)
# print(fun)
# print('function ended')

        ###     sum=15,multiply=50
        ###     function ended


''' ARBITARY (*) '''
# def find_sum(*num):
#      result=0
#      for i in num:
#         result=result+i
#      print('sum =',result)

# find_sum(1,2,3)

          ## sum = 6 ##


''' KEYWORD ARGUMENTS (=) '''

# def full_name(first_name,last_name):
#     print('First Name:',first_name)
#     print('Last Name',last_name)

# full_name(last_name='KARAN',first_name='HARI')

                ###    First Name: HARI
                ###    Last Name KARAN
# def addNum(a,b):
#     sum=a+b
#     mul=a*b
#     return f"sum={sum},multiply={mul}"
    
   

# fun=addNum(b=10,a=5)
# print(fun)
# print('function ended')


''' ARBITARY KEYWORD ARGUMENTS (**) "COMBINATION OF ARBITARY AND KEYWORD" '''
# def Student(**stud):
#     print('Name:'+stud['Name'])

# Student(Name='HARI',age=22)

             ##  Name:HARI  ##


''' PASSING LIST '''
''' PRINT ODD NUMBERS FROM THE LIST '''

# def odd_num(num):
#     for i in num:
#         if i%2==1:
#             print(i,end=' ')
# box=[1,2,3,4,5,6,7,8,9]

# odd_num(box)

          ##  1 3 5 7 9  ##


'''EXTRACT VOWELS FROM A STRING'''
# def vowels():
#     n=input('ENTER THE SENTENCE :')
#     l=[]
#     for i in n:
#         if i in 'aeiouAEIOU':
#             print(i,end=' ')

# vowels()

             ##ENTER THE SENTENCE :i love my country
             ##i o e o u


'''ANONYMOUS FUNCTIONS'''
'''lambda''' "used for small problems"
# sum=lambda x,y:x+y;

# print('VALUE OF TOTAL :',sum(10,20))

          ## VALUE OF TOTAL : 30 ##


'''scope of variable'''"variables will not not be defined(local) due to inside the function"
# def sum(x,y):
#     total = x+y
#     print('inside the function local total :',total)
#     return total;

# sum(10,20);
# print(total)
        ## inside the function local total : 30 ##

'''scope of variable will be globally'''
# total=20
# def sum(x,y):
#     total = x+y
#     print('inside the function local total :',total)
#     return total;

# sum(10,20);
# print(total)

         ##inside the function local total : 30
         ## 20


'''variables will be globally outside the function'''
# def sum(x,y):
#     total = x+y
#     print('inside the function local total :',total)
#     return total;

# sum(10,20);
# total=20
# print(total)

         ##inside the function local total : 30
         ## 20


'''Recursive functions''' "function inside function" "used in factrioal"
# def fact(n):
#     if n == 1:
#         return 1
#     else:
#         return(n*fact(n-1))
    
# print(fact(3))

           ## 6 ##



'''map()''' "easy method to sovle list,tuple,set by coverting"
# def calculateSquare(n):
#     return n*n

# numbers=(1,2,3,4)
# result=map(calculateSquare,numbers)
# print(list(result))

         ## [1, 4, 9, 16] ##


'''map() by lambda and converted to set'''
# num=(1,2,3,4,5)
# result=map(lambda i:i*i,num)
# print(set(result))

           ## {1, 4, 9, 16, 25} ##


'''mutiple iterators to map()'''
# num1=[4,5,6]
# num2=[1,2,3]
# result=map(lambda x,y:x+y,num1,num2)
# print('num3=',list(result))

          ##  num3= [5, 7, 9]  ##


'''filter ilteror conditions'''
'''extract vowels'''
# letters=['z','x','e','s','d','c','b','u','y','o']

# def filter_vowels(letter):
#     vowels=['a','e','i','o','u']
#     return True if letter in vowels else False
# filter_vowels=filter(filter_vowels,letters)

# print('vowels=',tuple(filter_vowels))

         ## vowels= ('e', 'u', 'o') ##

'''extact even numbers'''
# num=[1,2,3,4,5,6,7,8,9,0]

# def even(num):
#     return num%2==0

# filter_even=filter(even,num)

# print('even numbers=',tuple(filter_even))

         ## even numbers= (2, 4, 6, 8, 0) ##

'''using lambda'''
# num=[1,2,3,4,5,6,7,8,9,0]
# result=filter(lambda i:i%2==0,num)

# print('even numbers=',tuple(result))

          ## even numbers= (2, 4, 6, 8, 0) ##


'''._doc_ "to print the command in a function"'''
# def square(n):
#     '''take in a number n, returns the square of n'''
#     return n**2

# print(square.__doc__)

           ## take in a number n, returns the square of n ##



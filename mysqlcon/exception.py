'''a=5
b=0
c=a/b
print(c)'''

#ZeroDivisionError: division by zero

'''a=[1,2,3,4,5]
print(a[8])'''

#IndexError: list index out of range

'''handling errors---raising an exception'''
# x=10
# if x>5:
#     raise Exception('x should not exceed 5. The value of x was:{}'.format(x))


##   Exception: x should not exceed 5. The value of x was:10 ##

'''try--problem and except--message'''
# try:
#     n=10
#     d=0

#     result=n/d
#     print(result)

# except:
#     print('Error : DENOMINATOR CANNOT BE 0')

##Error : DENOMINATOR CANNOT BE 0 ##

'''first error will work next will not work'''
# try:
#     even_num=[2,4,6,8]
#     print(even_num[5])
#     a=5/0
#     print(a)

# except ZeroDivisionError:
#     print('denominator cannot be zero')

# except IndexError:
#     print('index out of bound.')

           ##index out of bound.##


'''try with else  , " assert---if like'''
# try:
#     num=int(input('ENTER THE NUMBER :'))
#     assert num%2 ==0

# except:
#     print('NOT A EVEN NUMBER!')

# else:
#     reciprocal=1/num
#     print(reciprocal)

          ##ENTER THE NUMBER :5
          ##NOT A EVEN NUMBER!

          ##ENTER THE NUMBER :6
          ##0.16666666666666666

'''try with finally---last answer'''
# try:
#     n=10
#     d=0

#     result=n/d
#     print(result)

# except:
#     print('Error : DENOMINATOR CANNOT BE 0')

# finally:
#     print('PROBLEM IS CLOSED')

         ##Error : DENOMINATOR CANNOT BE 0
         ##PROBLEM IS CLOSED

         #5.0                 #####if d=2
         #PROBLEM IS CLOSED

''''''


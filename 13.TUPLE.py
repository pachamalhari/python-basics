a=('HARI',22,'thamarassery')

#type 
'''print(type(a))'''

'''<class 'tuple'>'''


#comma is important
b='abc',
'''print(type(b))'''

'''<class 'tuple'>'''


#print 3th element
'''print(a[2])'''

'''thamarassery'''

#last element
'''print(a[-1])'''

'''thamarassery'''

#adding
'''print(a+b)'''

'''('HARI', 22, 'thamarassery', 'abc')'''

#create nested tuple
'''c=(a,b)
print(c)'''

'''(('HARI', 22, 'thamarassery'), ('abc',))'''
#nested tuple
'''d=(('HARI', 22, 'thamarassery'), ('abc',))'''

'''print(d[0][1])'''

'''22'''

#length

'''print(len(a))'''

'''3'''

#check
'''print(22 in a)'''

'''True'''

#repeat
'''m=('abc',)*3
print(m)'''

'''('abc', 'abc', 'abc')'''


#without comma
'''m=('abc')*3
print(m)'''

'''abcabcabc'''


#tuple is immutable

'''a=('HARI',2,'thamarassery',50,40)'''
'''a[1]=4
print(a)'''

''''tuple' object does not support item assignment'''

#delete tuple
'''del a[0]
print(a)'''

''' 'tuple' object doesn't support item deletion'''

#append tuple
'''a.append(3)
print(a)'''

''''tuple' object has no attribute 'append' '''

#remove tuple
'''a.remove('HARI')
print(a)'''

''' 'tuple' object has no attribute 'remove' '''

#tuple to list to mutable
'''y=list(a)
y.remove('HARI')
x=tuple(y)
print(x)'''

'''(2, 'thamarassery', 50, 40)'''


#unpacking tuple
'''tuple1=(1,2,3,4,5,)
a,b,c,d,e=tuple1
print(a,b,c,d,e)'''

'''1 2 3 4 5 '''

#branch
'''tupl=(1,1,2,98,400,500)'''
'''a,*b,c=tupl
print(a,b,c)'''

'''17 [1, 2, 98, 400] 500 '''

#index()

'''print(tupl.index(98))'''
#for loop
'''
for i in tupl:
    print(i)'''
'''
1
1
2
98
400
500
'''

#using range we need len

'''for i in range(len(tupl)):
    print(tupl[i])'''
'''
1
1
2
98
400
500
'''

#using while loop
'''
i=0
while i<len(tupl):
    print(tupl[i])
    i+=1'''
'''    
1
1
2
98
400
500
'''

#zip

'''first_name=('HARI','RAHUL','ANUSHIYA')
second_name=('KARAN','P','SHIJO')
age=(22,21,21)
combine=zip(first_name,second_name,age)
print(list(combine))'''

'''<zip object at 0x0000022D84697EC0>'''

'''[('HARI', 'KARAN', 22), ('RAHUL', 'P', 21), ('ANUSHIYA', 'SHIJO', 21)]'''









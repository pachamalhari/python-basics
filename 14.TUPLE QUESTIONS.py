#Q1.reverse the tuple
'''a=(1,2,3,4,5)'''
'''print(a[::-1])
(6, 5, 4, 3, 2, 1)'''

#Q2. access value 20 from the tuple which should be 5th item
'''b=list(a)
b.insert(4,20)
x=tuple(b)
print(x)'''
'''(1, 2, 3, 4, 20, 5, 6)'''

#Q3.create a tuple with single item 50
'''c=(50,)
print(type(c))'''
'''<class 'tuple'>'''

#Q4.Unpacking the tuple in 4 variables
'''x,y,z,*u=a
print(x,y,z,u)'''
'''1 2 3 [4, 5]'''

#Q5.swaping
'''b=(10,20,30,40,50)'''
'''a,b=b,a
print(a,b)'''

'''(10, 20, 30, 40, 50) (1, 2, 3, 4, 5)'''

#Q6.copy specfic element from one to new tuple

'''y=list(a)
del y[2]
u=tuple(y)
print(u)
x=list(b)
x.insert(2,y[3])
z=tuple(x)
print(z)'''


'''(1, 2, 4, 5)
(10, 20, 5, 30, 40, 50)'''

#Q8.sorted
'''q=(1,4,6,5,7,8)'''

'''y=sorted(q)
print(y)'''

'''[1, 4, 5, 6, 7, 8]'''

#reverse sorted

'''y=sorted(q,reverse=True)
print(y)'''

'''[8, 7, 6, 5, 4, 1]'''

#Q9.count
'''w=(1,1,3,5,5,67,77,8,8)
print(w.count(1))'''

'''2'''





#LIST
'''a=[3,5,9,'HARI']
print(type(a))'''

'''<class 'list'>'''

#PRINT SPECFIC ELEMENT
'''a=[3,5,9,'HARI']
print(a[3])'''

'''HARI'''

#CHECK HOW MANY ELEMENTS IN LIST
'''a=[3,5,9,'HARI']
print(len(a))'''

'''4 '''

#DELETE A ELEMENT
'''a=[3,5,9,'HARI']
del a[2]
print(a)'''

'''[3, 5, 'HARI']'''

#CLEAR DATA IN LIST
'''a=[3,5,9,'HARI']
a.clear()
print(a)'''

'''[]'''

#CONCATENATION
'''a=[3,5,9,'HARI']
b=['RAHUL',9,8,10]
print(a+b)'''

'''[3, 5, 9, 'HARI', 'RAHUL', 9, 8, 10]'''

#REPITATION
'''a=[3,5,9,'HARI']
c=a*3
print(c)'''

'''[3, 5, 9, 'HARI', 3, 5, 9, 'HARI', 3, 5, 9, 'HARI']'''

#CHECK THE ELEMENT IS PRESENT OR NOT(MEMBERSHIP OPERATOR)
'''a=[3,5,9,'HARI']
if 5 in a:
    print('5 is present')
else:
    print('not present')'''

#USING ELEMENT PRINT ALL ELEMENTS
'''a=[3,5,9,'HARI']
for i in a:
    print(i)'''

'''3
5
9
HARI '''

#USING RANGE PRINT ALL ELEMENTS
'''a=[3,5,9,'HARI']
for i in range(len(a)):
    print(a[i])'''
'''
3
5
9
HARI '''

#PRINT THE LAST ELEMENT IN THE LIST
'''a=[3,5,9,'HARI']
print(a[-1])'''

'''HARI'''

#######SLICING########
'''d=[3,5,6,9,10,23,89,99]'''

#PRINT THE LIST FROM 1 TO 5 ELEMENTS
'''print(d[1:5])'''

'''[5, 6, 9, 10] '''

#PRINT THE LIST FROM 1 TO 5 ELEMENTS AND SKIP BY 2 ELEMENTS
'''print(d[1:5:2])'''

'''[5, 9]'''

#PRINT THE LIST UPTO 7 ELEMENTS
'''print(d[:7])'''

'''[3, 5, 6, 9, 10, 23, 89]'''

#PRINT THE LIST FROM 4 TH ELEMENT
'''print(d[4:])'''

'''[10, 23, 89, 99]'''

#PRINT THE LIST FROM LAST ELEMENT
'''print(d[-1:-5:-1])

[99, 89, 23, 10]'''

#PRINT THE LIST FROM REVERSE ORDER
'''print(d[::-1])'''

'''[99, 89, 23, 10, 9, 6, 5, 3]'''

#ADD A ELEMENT IN THE LAST
'''d.append(17)
print(d)'''

'''[3, 5, 6, 9, 10, 23, 89, 99, 17]'''

#ADD ELEMENTS IN LIST WITH LIMIT
'''a=[]
n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    c=(input('ENTER THE ELEMENT :'))
    a.append(c)
print(a)'''

'''ENTER THE LIMIT :3
ENTER THE ELEMENT :2
ENTER THE ELEMENT :1
ENTER THE ELEMENT :5
['2', '1', '5'] '''

#ADD THE IN LIST IF IT IS EVEN
'''a=[]
n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    c=int(input('ENTER THE ELEMENT :'))
    if c%2==0:
        a.append(c)
print(a)'''

'''ENTER THE LIMIT :4
ENTER THE ELEMENT :3
ENTER THE ELEMENT :2
ENTER THE ELEMENT :5
ENTER THE ELEMENT :4
[2, 4]'''

#CHECK THE ELEMENT HOW MUCH TIME REPEATED
''''a=[1,3,4,6,5,7,9,7,5,42,44,6]
print(a.count(7))'''

'''2'''

#CHECK THE MAX AND MIN OF LISIT
'''a=[1,13,56,78,45,97,13,5]
print(min(a))
print(max(a))'''


'''
1
97
'''

#INSERT A ELEMENT IN LIST
'''a=['HARI','RAHUL','SARASWATHY']
a.insert(2,'PACHAMAL')
print(a)'''

'''['HARI', 'RAHUL', 'PACHAMAL', 'SARASWATHY']'''

#DELETE A ELEMENT IN LIST
'''a=['car', 'ball' , 'apple', 'fish']
a.remove('apple')
print(a)
['car', 'ball', 'fish']'''

#pop
'''a=['car', 'ball' , 'apple', 'fish']
a.pop(2)
print(a)
['car', 'ball', 'fish']'''

#pop zero
'''a=['car', 'ball' , 'apple', 'fish']
a.pop()
print(a)'''

'''['car', 'ball', 'apple']'''


#LIST COMPREHENSION
'''a=[1,2,3,4,5,6]
s=[i*2 for i in a]
print(s)'''

'''[2, 4, 6, 8, 10, 12]'''

# lisit and user input muliticatiom
'''a=[1,2,3,4,5,6,7,8,9,10]
e=int(input('ENTER THE ELEMENT FOR MULTIPLY : '))
s=[i*e for i in a]
print(s)'''

'''ENTER THE ELEMENT FOR MULTIPLY : 10
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]'''

#even numbers

'''a=[i for i in range(1,50) if i%2==0]
print(a)'''


'''[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]'''






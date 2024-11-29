#Q1
'''li = [100, 200, 300, 400, 500]
a.print second element
	b.print last element
	c.reverse the list
    d.print the type of 'li'''


#a.
'''print(li[1])'''

'''200'''

#b.
'''print(li[-1])'''

'''500'''

#c.
'''print(li[::-1])'''

'''[500, 400, 300, 200, 100]'''

#d.
'''print(type(li))'''

'''<class 'list'>'''


#Q2.Enter two list and perform concatination
'''a=[1,3,5,7,9,11]
b=[2,4,6,8,10]
print(a+b)'''

'''[1, 3, 5, 7, 9, 11, 2, 4, 6, 8, 10]'''

#Q3.Write a program to turn every item of a list into its square.
'''a=[1,3,5,7,9,11]
c=[i*i for i in a]
print(c)'''

'''[1, 9, 25, 49, 81, 121]'''

#Q4..Concatenate two lists in the following order
''' inputs  :
  	list1 = ["Hello ", "take "]
  	list2 = ["Dear", "Sir"] 
expected output:
    ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir'] '''

'''list1= ['HELLO ', 'TAKE']
list2= ['DEAR', 'SIR']
e=[]
for i in list1:
    for j in list2:
        k=i+j
        e.append(k)
print(e)'''

'''['HELLO DEAR', 'HELLO SIR', 'TAKEDEAR', 'TAKESIR']'''


#Q5..Write a program to add item 70 after 60 in the following Python List
'''li = [10, 20,50,60,30, 40]
li.insert(4,70)
print(li)'''

'''[10, 20, 50, 60, 70, 30, 40]'''


#Q7.Given a Python list, write a program to remove all occurrences of item 20.
'''list1 = [5, 20, 15, 20, 25, 50, 20]

del list1[1]
del list1[2]
del list1[4]
print(list1)'''

'''[5, 15, 25, 50]'''

#Q8.Write a Python program to sum all the items in a list.
'''li = [10, 20,50,60,30, 40]

total=sum(li)
print('total sum =',total)'''

'''total sum = 210'''

#Q9.Write a Python program to get the largest number from a list.
'''li = [10, 20,50,60,30, 40]

print(max(li))'''

'''60'''


#Q13.Deleting items (blue,green) in a list using 'del' keyword
'''colorList = ["Red","Blue","Green","Yellow","Orange","Purple"]

del colorList[1]
del colorList[1]
print(colorList)'''

'''['Red', 'Yellow', 'Orange', 'Purple']'''






#Q14.
'''list1=['apple','banana','mulberry',['cherry',['cashew','litchi',['tomato','chilli','ginger'],'grapes'],'lemon'],'mango','orange']'''
'''print(list1)
print(len(list1))'''

#a print mango
'''print(list1[4])'''

'''mango'''
# b print chilli
'''print(list1[3][1][2][1])'''

'''chilli'''

#c mulbery
'''print(list1[2])'''

'''mulberry'''

#d lemon
'''print(list1[3][2])'''

'''lemon'''

#e ginger
'''print(list1[3][1][2][2])'''

'''ginger'''

#f tomato ,chilli ginger
'''print(list1[3][1][2])'''

'''['tomato', 'chilli', 'ginger']'''

#cherry to lemon
'''print(list1[3])'''
'''['cherry', ['cashew', 'litchi', ['tomato', 'chilli', 'ginger'], 'grapes'], 'lemon']'''





#Q15.
'''a=[10,20,30,40,50,60,70,80,90,100]'''

'''print(a[2:5])'''
'''[30, 40, 50]'''

'''print(a[:4])'''
'''[10, 20, 30, 40]'''

'''print(a[3:])'''
'''[40, 50, 60, 70, 80, 90, 100]'''

'''print(a[-6])'''
'''50'''

'''print(a[1:4])'''
'''[20, 30, 40]'''

'''print(a[:5])'''
'''[10, 20, 30, 40, 50]'''

'''print(a[2:])'''
'''[30, 40, 50, 60, 70, 80, 90, 100]'''

'''print(a[:])'''
'''[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]'''

'''print(a[::])'''
'''[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]'''

'''print(a[::-1])'''
'''[100, 90, 80, 70, 60, 50, 40, 30, 20, 10]'''

'''print(a[::-2])'''
'''[100, 80, 60, 40, 20]'''




#Q16.input limit and insert value in middle
'''
a=[]
n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    c=int(input('ENTER THE ELEMENT :'))
    a.append(c)
print(a)
e=int(input('ENTER THE ELEMENT TO ADD : '))
a.insert(n//2,e)
print(a)'''
'''
ENTER THE LIMIT :4
ENTER THE ELEMENT :3
ENTER THE ELEMENT :2
ENTER THE ELEMENT :1
ENTER THE ELEMENT :1
[3, 2, 1, 1]
ENTER THE ELEMENT TO ADD : 5
[3, 2, 5, 1, 1]'''

#Q17.Create a list using user input function after print the list convert element into two separte list as odd list and even list.
'''x = int(input("enter the limit"))
y =[]
for i in range(x):
    z = int(input("enter element:"))
    y.append(z)
even=[]
odd=[]
for i in y:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print('ORIGINAL LIST',y)
print('EVEN LIST',even)
print('ODD LIST',odd)'''

'''ORIGINAL LIST [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
EVEN LIST [2, 4, 6, 8, 10]
ODD LIST [1, 3, 5, 7, 9]'''




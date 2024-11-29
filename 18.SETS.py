#no repiatation
'''a={1,1,3,4,5,6,6,2,4}
print(a)'''

'''{1, 2, 3, 4, 5, 6}'''


#boolean value "true or 1"
'''a={True,333,3,14,15,6,6,2,4,1,False,0}
print(a)'''

'''{False, True, 2, 3, 4, 6, 333, 14, 15}'''


#type
'''a={True,333,3,14,15,6,6,2,4,1,False,0}
print(type(a))'''

'''<class 'set'>'''


#length
'''a={True,333,3,14,15,6,6,2,4,1,False,0}
print(len(a))'''

'''9'''


#for loop
'''a={True,333,3,14,15,6,6,2,4,1,False,0}
for i in a:
    print(i)'''
'''    
False
True
2
3
4
6
333
14
15'''


#add() item in set
'''a={True,333,3,14,15,6,6,2,4,1,False,0}
a.add('apple')
print(a)'''

'''{False, True, 2, 3, 4, 6, 333, 14, 15, 'apple'}'''

#update() " to add two sets together"
'''a={1,2,6,8}
b={'apple','cherry'}
a.update()
print(a)'''

'''{1, 2, 'apple', 'cherry', 6, 8}'''


#list/tuple/string can be add to set
'''a=[1,2,6,8]
b={'apple','cherry'}
b.update(a)
print(b)'''

'''{1, 2, 6, 8, 'cherry', 'apple'}'''


#remove() a item from set
'''a={1,2,6,8}
a.remove(2)
print(a)'''

'''{8, 1, 6}'''

#discard() "same as remove"
'''a={1,2,6,8}
a.discard(2)
print(a)'''

'''{8, 1, 6}'''

#pop() "random remove a item"
'''a={1,2,6,8}
y=a.pop()
print(a)
print(y)'''

'''{1, 2, 6}
8 '''

#clear()
'''a={1,2,6,8}
a.clear()
print(a)'''

'''set()'''  "set constructor"

#union() " 3rd set intial to add two sets together" not like update()
'''a={1,2,6,8}
b={'apple','cherry'}
c=a.union(b)
print(c)'''

'''{'cherry', 1, 2, 6, 8, 'apple'}'''

#intersection_update " take common item" intersection_update() to reduce 3rd set
'''a={1,2,6,8,'apple'}
b={'apple','cherry'}
a.intersection_update(b)
print(a)'''

'''{'apple'}'''

#intersection() "3rd new set is needed"
'''a={1,2,6,8,'apple'}
b={'apple','cherry'}
c=a.intersection(b)
print(c)'''

'''{'apple'}'''

#symmertic_difference() "opposite of intersection" "common will not come"
'''a={1,2,6,8,'apple'}
b={'apple','cherry'}
c=a.symmetric_difference(b)
print(c)'''

'''{1, 2, 'cherry', 6, 8}'''

#symmetric_difference_update() "no need new set"
'''a={1,2,6,8,'apple'}
b={'apple','cherry'}
a.symmetric_difference_update(b)
print(a)'''

'''{1, 2, 6, 8, 'cherry'}'''


#difference "common will not come in first set"
'''a={1,2,6,8,'apple'}
b={'apple','cherry'}
c=a.difference(b)
print(c)'''

'''{8, 1, 2, 6}'''

#difference_update " no need new set"
'''a={1,2,6,8,'apple'}
b={'apple','cherry'}
a.difference_update(b)
print(a)'''

'''{1, 2, 6, 8}'''




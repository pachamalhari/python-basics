#Q1.Add a list of elements to a set.
'''a=[1,22,333,444]
b={'apple','orange','mango'}
b.update(a)
print(b)'''

'''{1, 333, 'apple', 22, 'mango', 444, 'orange'}'''

#Q2.Return a new set of identical items from two sets.
'''a={1,22,333,444,'apple'}
b={'apple','orange','mango'}
a.intersection_update(b)
print(a)'''

'''{'apple'}'''

#Q3.Get Only unquie item from two sets.
'''a={1,22,333,444,'apple'}
b={'apple','orange','mango'}
a.symmetric_difference_update(b)
print(a)'''

'''{1, 'orange', 22, 'mango', 444, 333}'''

#Q4.Update the first set with item that don't exist in the second set.
'''a={1,22,333,444,'apple'}
b={'apple','orange','mango'}
a.add('plum')
print(a)'''

'''{1, 22, 'apple', 'plum', 444, 333}'''

#Q5.Remove items from the set at once.
'''a={1,22,333,444,'apple'}
a.remove(22)
print(a)'''

'''{1, 'apple', 444, 333}'''

#Q6.Return a set of elements present in Set A or Set B, but not both
'''a={1,22,333,444,'apple'}
b={'apple','orange','mango'}
a.difference_update(b)
print(a)'''

'''{1, 22, 444, 333}'''

#Q7.Check if two sets have any elements in common. If yes, display the common elements.
'''a={1,22,333,444,'apple'}
b={'apple','orange','mango'}
a.intersection_update(b)
print(a)'''

'''{'apple'}'''

#Q8.Update Set1 by adding items from Set2,except common items.
'''a={1,22,333,444,'apple'}
b={'apple','orange','mango'}
a.update(b)
print(a)'''

'''{'apple', 1, 'mango', 22, 'orange', 444, 333}'''

#Q9.Remove items from set1 that are not common to both set1 and set2.
'''a={1,22,333,444,'apple'}
b={'apple','orange','mango'}
a.intersection_update(b)
print(a)'''

'''{'apple'}'''

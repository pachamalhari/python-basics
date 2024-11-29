#dictionary
'''d={'name':'HARI','age':22,'place':'kozhikode'}
print(d)
print(d['name'])'''

'''{'name': 'HARI', 'age': 22, 'place': 'kozhikode'}
HARI'''


#no dupilcate allowed "new value updated
'''d={'name':'HARI','age':22,'place':'kozhikode','age':25}
print(d)'''

'''{'name': 'HARI', 'age': 25, 'place': 'kozhikode'}'''


#length
'''d={'name':'HARI','age':22,'place':'kozhikode'}
print(len(d))'''

'''3'''


#type
'''d={'name':'HARI','age':22,'place':'kozhikode'}
print(type(d))'''

'''<class 'dict'>'''


#check empty set 
'''d={}
print(type(d))'''

'''<class 'dict'>'''


#another method to check type
'''d=dict()
print(type(d))'''

'''<class 'dict'>'''


#Square 
'''d=dict()
for i in range(1,11):
    f={i:i*i}
    d.update(f)
print(d)'''

'''{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}'''


#add list in dictionary
'''d={'name':'HARI','age':22,'place':'kozhikode'}
d['hobbies']=['cricket','reading']
print(d)'''

'''{'name': 'HARI', 'age': 22, 'place': 'kozhikode', 'hobbies': ['cricket', 'reading']}'''


#dict() constructor
'''d=dict(name='HARI',age=22,country='INDIA')
print(d)'''

'''{'name': 'HARI', 'age': 22, 'country': 'INDIA'}'''


#get() "to get a single key"
'''d={'name':'HARI','age':22,'place':'kozhikode'}
print(d.get('place'))'''

'''kozhikode'''


#keys to find
'''d={'name':'HARI','age':22,'place':'kozhikode'}
f=d.keys()
print(f)'''

'''dict_keys(['name', 'age', 'place'])'''


#values to find
'''d={'name':'HARI','age':22,'place':'kozhikode'}
f=d.values()
print(f)'''

'''dict_values(['HARI', 22, 'kozhikode'])'''


#dict to tuple items "value pairs"
'''d={'name':'HARI','age':22,'place':'kozhikode'}
f=d.items()
print(f)'''

'''dict_items([('name', 'HARI'), ('age', 22), ('place', 'kozhikode')])'''


#update "update key"
'''d={'name':'HARI','age':22,'place':'kozhikode'}
d.update({'age':23})
print(d)'''

'''{'name': 'HARI', 'age': 23, 'place': 'kozhikode'}'''


#new key add "use update"
'''d={'name':'HARI','age':22,'place':'kozhikode'}
d.update({'country':"INDIA"})
print(d)'''

'''{'name': 'HARI', 'age': 22, 'place': 'kozhikode', 'country': 'INDIA'}'''


#pop "remove"
'''d={'name':'HARI','age':22,'place':'kozhikode'}
d.pop('place')
print(d)'''

'''{'name': 'HARI', 'age': 22}'''


#popitem "remove last item"
'''d={'name':'HARI','age':22,'place':'kozhikode'}
d.popitem()
print(d)'''

'''{'name': 'HARI', 'age': 22}'''


#del "remove"
'''d={'name':'HARI','age':22,'place':'kozhikode'}
del d['place']
print(d)'''

'''{'name': 'HARI', 'age': 22}'''


#clear()
'''d={'name':'HARI','age':22,'place':'kozhikode'}
d.clear()
print(d)'''

'''{}'''




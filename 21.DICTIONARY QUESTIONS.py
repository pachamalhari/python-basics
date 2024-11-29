#Q1.Print "80" from the given sampleDict    ##"nested dictionary"##
'''sampleDict={"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
print(sampleDict["class"]["student"]["marks"]["history"])'''

'''80'''


#Q2.Output :{'a': ['am', 'america']} from the given string
'''q='I am from america i am america'
li=q.split()
d=[]
for i in li:
    if i[0]=='a' and i not in d:
        d.append(i)
w=dict(a=d)
print(w)'''

'''{'a': ['am', 'america']}'''


#Q3.Print the words corresponding to the first letter of the word has a key in dictionary
'''q='python is a programming langauge'
li=q.split()
d={}
for i in li:
    x=i[0].lower()
    if x not in d:
        d[x]=[]
    d[x].append(i) 
print(d)'''

'''{'p': ['python', 'programming'], 'i': ['is'], 'a': ['a'], 'l': ['langauge']}'''
#Q4.keys = ['Ten', 'Twenty', 'Thirty' ] values = [10, 20, 30] Output : Dict1={'Ten': 10, 'Twenty": 20, 'thirty': 30}  ##zip()##
'''keys = ['Ten', 'Twenty', 'Thirty' ]
values = [10, 20, 30]
Dict1=dict(zip(keys,values))
print(Dict1)'''

'''{'Ten': 10, 'Twenty': 20, 'Thirty': 30}'''    


#Q5.Contactbook which must be added in contact book : 1.Add a contact 2.Delete a contact 3.Edit a contact 4.Search a contact 5.List all contacts 6.Exit
print('1.Add a contact')
print('2.Delete a contact')
print('3.Edit a contact')
print('4.Search a contact')
print('5.List all contacts')
print('6.Exit')
x=(input('ENTER YOUR OPTION : '))
d={}
while x!='6':
    if x=='1':
        name=input('ENTER THE NAME TO ADD : ')
        phone=input('ENTER THE NUMBER TO ADD : ')
        d[name]=phone
        print('CONTACT IS ADDED SUCCESSFULLY!')
    elif x=='2':
        name=input('ENTER THE NAME TO DELETE : ')
        if name in d:
            d.pop(name)
            print('CONTACT IS DELETED SUCCESSFULLY!')
        else:
            print("CONTACT IS NOT FOUND!")
    elif x=='3':
        name=input('ENTER THE NAME TO EDIT : ')
        if name in d:
            new=input('ENTER THE NEW PHONE NUMBER :')
            d[name]=new
            print('CONTACT IS EDITED SUCCESSFULLY!')
        else:
            print("CONTACT IS NOT FOUND!")
    elif x=='4':
        name=input('ENTER THE NAME TO SEARCH : ')
        if name in d:
            print('PHONE NUMBER : ', d[name])
        else:
            print("CONTACT IS NOT FOUND!")
    elif x=='5':
        print('NAME : PHONE NUMBER')
        print('-'*30)
        for name,phone in d.items():
            print(name, ':', phone)
    else:
        print("INVALID OPTION.PLEASE CHOOSE THE CORRECT OPTION!")
    x=(input('ENTER YOUR OPTION : '))

#Q6.
number={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
value={1:'Ones',2:'Tens',3:'Hundreds',4:'Thousands',5:'Ten_Thousand',6:'Hundred_Thousands',7:'Millions',8:'Ten_Millions',9:'Hundred_Millions',10:'Billions'}
n=(input('Enter the number : '))
l=len(n)
result=''
for i in n:
    x=int(i)
    y=value[l]
    z=result+number[x]+y
    l-=1
    print(z,end=' ')
    
Enter the number : 4731
FourThousands SevenHundreds ThreeTens OneOnes 


#Q7.
    
    
        
        

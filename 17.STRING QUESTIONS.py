#Q1. print characters using split
'''y='Hello World!'
q=y.split()
for i in y:
    for j in i:
        print(j,end=' ')'''

'''H e l l o   W o r l d ! '''


#Q2.skip T to t
'''a='this is a big tree'
b=a.split()
for i in b:
    if i[0]==t:
        print(i)'''

#Q3.Write a pgm  that takes a string as input and returns the string in reverse order.
'''y=input('ENTER THE STRING YOU WANT TO REVERSE :')
rev=y[::-1]
print(rev)'''

'''ENTER THE STRING YOU WANT TO REVERSE :harikaran
narakirah'''


#Q4. Write a pgm  that takes a string as input and returns the largest size word in the string
'''y=input('ENTER THE STRING :')
q=y.split()
largest=[]
for i in q:
    if len(i)>len(largest):
        largest=len(i)
        largest=i
print('THE LARGERST WORD IN STRING IS : ',largest)'''

'''ENTER THE STRING :iam a hero
THE LARGERST WORD IN STRING IS :  hero'''


#Q5. Write a pgm that counts the number of vowels (a, e, i, o, u) in a given string.
'''y=input('ENTER THE STRING :')
count=0
vowels='aeiouAEIOU'
for i in y:
    if i in vowels:
        count+=1
print("NUMBER OF VOWELS: ",count)'''

'''ENTER THE STRING :harikaran
NUMBER OF VOWELS:  4 '''

#Q6. Address a string as user input then count the number of digits, alphabets and special characters.
'''y=input('ENTER THE STRING: ')
digit=0
alpha=0
special=0
for i in y:
    if i.isdigit():
        digit+=1
    elif i.isalpha():
        alpha+=1
    else:
        special+=1
print("Number of digits:", digit)
print("Number of alphabets:", alpha)
print("Number of special characters:", special)'''

'''ENTER THE STRING: dkGKwuh***@@12389
Number of digits: 5
Number of alphabets: 7
Number of special characters: 5'''

#Q7. Create a string and separte the lowercase and uppercase letter.
'''y=input('ENTER THE STRING: ')
upper=[]
lower=[]
for i in y:
    if i.isupper():
        upper.append(i)
    else:
        lower.append(i)
print('ORIGINAL STRING :',y)
print('UPPERCASE :',upper)
print('LOWERCASE :',lower)'''


'''ENTER THE STRING: claueUdslauSUA
ORIGINAL STRING : claueUdslauSUA
UPPERCASE : ['U', 'S', 'U', 'A']
LOWERCASE : ['c', 'l', 'a', 'u', 'e', 'd', 's', 'l', 'a', 'u']'''


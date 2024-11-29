#multi line string
'''
a="""Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has
been the industrys standard dummy text ever since the 1500s, when an unknown printer took a

galley of type and scrambled it to make a type specimen book. It has survived not only five centuries,
but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in
the 1960s with the release of """

print(a)'''

# for loop
'''
for i in 'HARI':
    print(i)
H
A
R
I
'''

#length
'''a='hari'
print(len(a))'''

'''4'''

#space counts
a='hello world'
'''print(len(a))'''

'''11'''

#check the string

'''print('world' in a)'''

'''True'''
#not in
'''print('world' not in  a)'''

'''False'''

#slicing
'''print(a[:5])'''

'''hello'''

'''print(a[::-1])'''

'''dlrow olleh'''

#captial alphabrt
'''print(a.upper())'''

'''HELLO WORLD'''

#lower alphabet
'''b='HELLO WORLD'''
'''print(b.lower())'''

'''hello world'''

#strip
'''c='    hello world'''
'''print(a.strip())'''

'''hello world'''

#replace
'''d='hheloo worldh'
print(d.replace('h','j'))'''

'''jjeloo worldj'''


#split
"""y='The split() method returns a list where the text between the specified separator becomes the list items.

print(y.split())

['The', 'split()', 'method', 'returns', 'a', 'list', 'where', 'the', 'text', 'between', 'the', 'specified', 'separator', 'becomes', 'the', 'list', 'items.']
print(y.split('t'))

['The spli', '() me', 'hod re', 'urns a lis', ' where ', 'he ', 'ex', ' be', 'ween ', 'he specified separa', 'or becomes ', 'he lis', ' i', 'ems.']"""

#write a program count the no. of words in a given string

y=' The split() method returns a list where the text between the specified separator becomes the list items.'

'''q=y.split()
print(q)
count=0
for i in q:
    count+=1
print(count)'''

'''17'''

#using len find the words
'''q=y.split()
for i in range(len(q)+1):
    pass
print(i)'''

'''17'''

#add numbers "format"
'''a=int(input('ENTER THE FIRST NUMBER : '))
b=int(input('ENTER THE SECOND NUMBER : '))
c=a+b
txt='THE SUM OF {} AND {} IS {}'.format(a,b,c)
print(txt)'''

#simple method
'''a=int(input('ENTER THE FIRST NUMBER : '))
b=int(input('ENTER THE SECOND NUMBER : '))
c=a+b
txt=f'THE SUM OF {a} AND {b} IS {c}'
print(txt)'''

#escape charater double inverted comma
'''txt="he \"HARI\" from the kerala"
print(txt)'''

#to print it's

'''txt='it\'s alright.'
print(txt)'''

'''it's alright.'''

#\n two lines
'''txt="hari\nkaran"
print(txt)'''

'''
hari
karan
'''


#\t big space
'''txt="hari\tkaran"
print(txt)'''

'''hari	karan'''

#\b backspace but not use in idle
'''txt="hari\bkaran"
print(txt)'''

'''harikaran'''

#capitalize() "first word letter is capital"
'''txt='iam a hero'
y=txt.capitalize()
print(y)'''

'''Iam a hero'''


#title() "first letter of all words is capital"
'''txt='iam a hero.superman'
y=txt.title()
print(y)'''

'''Iam A Hero.Superman'''

#casefold "all will be small letter
'''txt='Iam A Hero,Superman'
y=txt.casefold()
print(y)'''

'''iam a hero,superman'''

#center 
'''name='Hari'
y=name.center(20,'o')
print(y)'''

'''ooooooooHarioooooooo'''

#count()
'''txt='iam a superhero'
y=txt.count('e')
print(y)'''

'''2'''


#count() @position
'''txt='iam a superhero'
y=txt.count('e',5,10)
print(y)'''

'''1'''

#check it is end with "endswith()"
'''txt='iam a superhero'
y=txt.endswith('.')
print(y)'''

'''False'''
#true statement
'''txt='iam a superhero'
y=txt.endswith('superhero')
print(y)'''

'''True'''

#startswith() " check startswith"
'''txt='iam a superhero'
y=txt.startswith('superhero')
print(y)'''

'''False'''

#find() "to find the word and gives index number" if no -1
'''txt='iam a superhero'
y=txt.find('m')
print(y)'''

'''2'''

###if no
'''txt='iam a superhero'
y=txt.find('z')
print(y)'''

'''-1'''


#index() "to find the word and gives index number" if no error will show
'''txt='iam a superhero'
y=txt.index('m')
print(y)'''

'''2'''

###if no
'''txt='iam a superhero'
y=txt.index('z')
print(y)'''

'''ValueError: substring not found'''

#isalnum() "check only alphanumeric " if special characters and space present it will show false
'''txt='Abc123'
q=txt.isalnum()
print(q)'''

'''True'''

#isalpha "only alphabets"
'''txt='Abcd'
q=txt.isalpha()
print(q)'''

'''True'''

#isdigit "only numeric"
'''txt='1234'
q=txt.isdigit()
print(q)'''

'''True'''

#swapcase() "opposite of what we given"
'''txt='Iam A SuperHero'
y=txt.swapcase()
print(y)'''

'''iAM a sUPERhERO'''

#maketrans() and translate() to replace the word
'''txt='Iam A SuperHero'
y=txt.maketrans('S','p')
print(txt.translate(y))'''

'''Iam A puperHero'''

#####join#### "replace space to star"
'''txt='this is oneteam'
y=txt.split()
a='*'.join(y)
print(a)'''

'''this*is*oneteam'''

####remove space##
'''txt='this is oneteam'
y=txt.split()
a=''.join(y)
print(a)'''

'''thisisoneteam'''


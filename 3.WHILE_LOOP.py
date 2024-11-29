#PRINT 10 TO 50
'''i=10
while i<=50:
    print(i)
    i+=1'''


# PRINT THE SUM OF 1 TO 10
'''sum=0
i=1
while i<=10:
    sum=sum+i
    i+=1
print(sum)'''


#FACTORIAL
'''i=int(input('ENTER THE NUMBER = '))
fact=1
while i>=1:
    fact=fact*i
    i-=1
print(fact)'''


#EXPANDED FACTORIAL
'''i=int(input('ENTER THE NUMBER = '))
fact=1
while i>=1:
    fact=fact*i
    i-=1
    print(fact,end='x')'''


#PRINT EVEN NUMBERS B/W 1 TO 100
'''i=0
while i<100:
    if i%2==0: 
        print(i)
    i+=2'''


#PRINT EVEN NUMBERS B/W 1 TO 100 BUT INGERTMENT BY 1
'''i=1
while i<100:
    if i%2==0:
        print(i)
    i+=1'''


#PRINT THE ODD NUMBER BUT INGERMENT BY 1
'''n=int(input('ENTER THE LIMIT ='))
i=0
while i<=n:
    if i%2==1:
        print(i)
    i+=1'''

#MUTIPLE OF 5 AND INGERMENT BY 1
'''n=int(input('ENTER THE LIMIT ='))
i=0
while i<=n:
    if i%5==0:
        print(i)
    i+=1'''


#MULTIPICATION TABLE
'''n=int(input('WHICH MUTILPICATION TABLE: '))
i=1
while i<=10:
    print(i,'x',n,'=',i*n)
    i+=1'''


#CHECK THE PRIME NUMBER
'''n=int(input('ENTER THE LIMIT ='))
i=2
while i<=n:
    if n%i==0:
        print('NOT A PRIME NUMBER')
    i+=1
    else:
        print(' A PRIME NUMBER')'''


#PRINT THE MULTIPLE OF 7 AND 5 FROM 1 TO 100
'''i=1
while i<=100:
    if i%7==0 or i%5==0:
        print(i)
    i+=1'''


#FIBINOCCI SEQUENCES
'''first=1
second=1
i=0
while i<=10:
    print(first,end=' ')
    sum=first+second
    first=second
    second=sum
    i+=1'''


#REVERSE NUMBER
'''a=int(input('ENTER THE NUMBER = '))
rev=0
while a!=0:
    digit=a%10
    rev=rev*10+digit
    a=a//10
print(rev)'''


#CHECK THE SEQUENCE IS PALINDROME
'''n=int(input('ENTER THE SEQUENCE'))
rev=0
temp=n
while n!=0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
    rev=temp
    print('IT IS PALINDROME')
else:
    print('NOT PALINDROME')'''

    


    

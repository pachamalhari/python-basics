#PRINT 1 TO 50
'''for i in range(1,51):
    print(i)'''


#PRINT THE SUM OF 1 TO 10
'''sum=0
for i in range(1,10):
        sum+=1
print(sum)'''


#FACTORIAL
'''i=int(input('ENTER THE NUMBER = '))
fact=1
for i in range(1,i+1):
    fact=fact*i
print(fact)'''


#EXPANDED FACTORIAL
'''i=int(input('ENTER THE NUMBER = '))
fact=1
for i in range(1,i+1):
    fact=fact*i
    print(fact,'x',end=' ')'''


#PRINT EVEN NUMBERS B/W 1 TO 100
'''for i in range(0,101,2):
    print(i)'''
#another method
'''for i in range(1,101):
    if i%2==0:
        print(i)'''


#PRINT THE ODD NUMBERS
'''for i in range(1,101):
    if i%2==1:
        print(i)'''


#MULTIPLY BY 5
'''n=int(input('ENTER THE LIMIT = '))
for i in range(1,n):
    if i%5==0:
        print(i)'''


#MUTLIPICATION TABLE
'''n=int(input('WHICH MUTILPICATION TABLE: '))
for i in range(1,11):
    print(i,'x',n,'=',i*n)'''


#CHECK THE PRIME NUMBER


#MULTIPICATION OF 7 OR 5 FROM 1TO 100
'''for i in range(1,101):
    if i%7==0 or i%5==0:
        print(i)'''


#ODD NUMBER SUM UP TO 20
'''sum=0
for i in range(1,20):
    if i%2==1:
        sum+=i
print(sum)'''


#FIND THE AVERAGE OF ENTER NUMBER
'''n=int(input('ENTER THE LIMIT : '))
sum=0
for i in range(n):
    c=int(input('ENTER THE VALUES: '))
    sum=(sum+c)/n
print(sum)'''


#2+22+222=246
'''a=(input('ENTER THE NUMBER='))
b=a+a
c=a+a+a
z=int(a)+int(b)+int(c)
for i in a:
    print(a,'+',b,'+',c,'=',z)'''


#FIBINOCCI SEQUENCE
'''n=int(input('ENTER THE NUMBER= '))
a=0
b=1
for i in range(1,n+1):
    print(a,end=' ')
    c=a+b
    a=b
    b=c'''


#REVERSE NUMBER
'''a=int(input('ENTER THE NUMBER= '))
rev=0
for i in range(a):
    if a!=0:
        digit=a%10
        rev=rev*10+digit
        a=a//10
print(rev)'''


#PALINDROME 





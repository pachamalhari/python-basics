#FIND THE BIGGER AMOUNG TWO NUMBERS
'''a=int(input('ENTER THE FIRST NUMBER = '))
b=int(input('ENTER THE SECOND NUMBER = '))
if a>b:
    print('FIRST is bigger than SECOND')
else:
    print('SECOND is bigger than FIRST')'''


#ELIGIBLE FOR VOTING
'''a=int(input('ENTER YOUR AGE = '))
if a>=18:
    print('YOUR ELIGIBLE FOR VOTING')
else:
    print('NOT ELIGIBLE')'''


#WHICH IS BIGGER AMOUNG THREE NUMBERS
'''a=int(input('ENTER THE FIRST NUMBER = '))
b=int(input('ENTER THE SECOND NUMBER = '))
c=int(input('ENTER THE THIRD NUMBER = '))
if a>b and a>c:
    print('FIRST NUMBER IS BIGGER')
elif b>a and b>c:
    print('SECOND NUMBER IS BIGGER')
else:
    print('THRID NUMBER IS BIGGER')'''


#CHECK NUMBER IS DIVISIBLE OF 3 OR 5
'''a=int(input('ENTER THE NUMBER = '))
if a%3==0:
    print('THE NUMBER IS DIVISIBLE BY 3')
    if a%5==0:
        print('DIVISIBLE BY 5')
    else:
        print('NOT DIVISIBLE BY 5')
else:
    print('THE NUMBER IS DIVISIBLE BY 5 AND NOT DIVISIBLE BY 3')'''


#CHECK NUMBER IS EVEN OR ODD NUMBER
'''a=int(input('ENTER THE NUMBER = '))
if a>0 and a%2==0:
    print('THE NUMBER IS EVEN AND POSTIVE')
else:
    print('THE NUMBER IS ODD AND NEGATIVE')'''


#CHECK THE NUMBER IS POSTIVE OR NEGATIVE
'''a=int(input('ENTER THE NUMBER = '))
if a>0:
    print('POSTIVE')
else:
    print('NEGATIVE')'''


#CHECK THE NUMBER IS EVEN OR POSTIVE OR NEGATIVE OR ODD
'''a=int(input('ENTER THE NUMBER = '))
if a%2==0:
    print('EVEN NUMBER')
    if a>0:
        print('ALSO POSTIVE NUMBER')
    else:
        print('ALSO NEGATIVE NUMBER')
else:
    print('ODD NUMBER')
    if a>0:
         print('ALSO POSTIVE NUMBER')
    else:
        print('ALSO NEGATIVE NUMBER')'''


#CHECK THE NUMBER IS POSTIVE OR NEGATIVE OR ZERO
'''a=int(input('ENTER THE NUMBER = '))
if a>0:
        print('POSTIVE NUMBER')
elif a<0:
    print('NEGATIVE NUMBER')
else:
    print('ZERO')'''


#FIND THE NET SALARY, IF ABOVE 10000 INCREASE 2 PERCENTAGE FOR EVERYTHING
'''bs=int(input('ENTER YOUR BASE SALARY = '))
if bs<=10000:
    hr=bs*(20/100)
    da=bs*(3/100)
    pf=bs*(15/100)
else:
    hr=bs*(22/100)
    da=bs*(5/100)
    pf=bs*(17/100) 
nt=bs+hr+da-pf
print('YOUR NET SALARY : ',nt)'''


#STUDENT MARK IS 90> A+ , 81 B/W 89 = A , 71 B/W 80 = B+ , 61 B/W 70 = B , <60 FAIL
'''m=int(input('ENTER THE MARK = '))
if m>=90:
    print('YOUR GRADE IS A+')
elif m>=81 and m<=89:
    print('YOUR GRADE IS A')
elif m>=71 and m<=80:
    print('YOUR GRADE IS B+')
elif m>=61 and m<=70:
    print('YOUR GRADE IS B')
else:
    print('YOUR FAILED')'''


#COLOUR CODE VIBGYOR
'''c=input('ENTER THE COLOUR CODE = ')
if c=='v' or c=='V':
    print('YOUR COLOUR IS VIOLET')
elif c=='i' or c=='I':
    print('YOUR COLOUR IS INDIGO')
elif c=='b' or c=='B':
    print('YOUR COLOUR IS BLUE')
elif c=='g' or c=='G':
    print('YOUR COLOUR IS GREEN')
elif c=='y' or c=='Y':
    print('YOUR COLOUR IS YELLOW')
elif c=='o' or c=='O':
    print('YOUR COLOUR IS ORANGE')
elif c=='r' or c=='R':
    print('YOUR COLOUR IS RED')
else:
    print('NO COLOUR FOUND')'''


#UNIT CONSUMED 0-100 0.50 PER UNIT , 101-200 RS 50 + 1 PER UNIT , 201-300 RS 150 + 1.50 PER UNIT , >300 RS 300 + 2 PER UNIT
'''u=int(input('ENTER THE UNIT CONSUMED = '))
if u>=0 and u<=100:
    c=u*0.50
    print('CHARGE FOR UNIT COUNSUMED = ',c)
elif u>=101 and u<=200:
    c=50+(u-100)*1
    print('CHARGE FOR UNIT COUNSUMED = ',c)
elif u>=201 and u<=300:
    c=150+(u-200)*1.50
    print('CHARGE FOR UNIT COUNSUMED = ',c)
else:
    c=300+(u-300)*2
    print('CHARGE FOR UNIT COUNSUMED = ',c)'''

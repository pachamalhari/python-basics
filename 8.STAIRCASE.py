#DOWNWARD STAR STAIRCASE
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(i):
        print('*',end=' ')
    print()'''

'''
ENTER THE LIMIT :7
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
'''

# MIRROR IMAGE OF DOWNWARD STAIR
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(n-i):
        print('*',end=' ')
    print()'''

'''
ENTER THE LIMIT :7
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
'''

#DOWN STAIR WITH NUMBERS INCREASES BY i
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(i):
        print(i,end=' ')
    print()'''

'''
ENTER THE LIMIT :7
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
6 6 6 6 6 6 
'''

#DOWN STAIR WITH NUMBERS INCREASES BY j
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(i):
        print(j+1,end=' ')
    print()'''

'''
ENTER THE LIMIT :7
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6
'''
    
#DOWN STAIR WITH ALPHABET INCRESASE BY i
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(i):
        print(chr(64+i),end=' ')
    print()'''

'''
ENTER THE LIMIT :7

A 
B B 
C C C 
D D D D 
E E E E E 
F F F F F F 
'''

#DOWN STAIR WITH ALPHABET INCREASE BY j
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(i):
        print(chr(65+j),end=' ')
    print()'''

'''
ENTER THE LIMIT :7

A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F 
'''

#UPWARD STAIR WITH SPACE AND STAR
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(1,n-i):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    print()'''

'''
ENTER THE LIMIT :7
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 
* * * * * * 
'''

#UPWARD STAIR WITH SPACE AND NUMBER
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(1,n-i):
        print(' ',end=' ')
    for k in range(i):
        print(i,end=' ')
    print()'''

'''
ENTER THE LIMIT :7
          1 
        2 2 
      3 3 3 
    4 4 4 4 
  5 5 5 5 5 
6 6 6 6 6 6 
'''

#UPWARD STAIR WITH SPACE AND NUMBER AND INCRESE WITH i
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(1,n-i):
        print(' ',end=' ')
    for k in range(i):
        print(chr(64+i),end=' ')
    print()'''
'''
ENTER THE LIMIT :7
          A 
        B B 
      C C C 
    D D D D 
  E E E E E 
F F F F F F 
'''

#MIRROR IMAGE OF UPWARD STAIR
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
        print('*',end=' ')
    print()'''

'''
ENTER THE LIMIT :7
  * * * * * * 
    * * * * * 
      * * * * 
        * * * 
          * * 
            *
'''



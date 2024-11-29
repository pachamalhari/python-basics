#PYRAMID
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(n-i):
        print('  ',end='')
    for k in range(i):
        print(' *  ',end='')
    print()'''
'''
ENTER THE LIMIT :7
              
             *  
           *   *  
         *   *   *  
       *   *   *   *  
     *   *   *   *   *  
   *   *   *   *   *   *  

'''

#ODD NUMBER PYRAMID
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(2*i+1):
        print('*',end=' ')
    print()'''
'''
ENTER THE LIMIT :7
              * 
            * * * 
          * * * * * 
        * * * * * * * 
      * * * * * * * * * 
    * * * * * * * * * * * 
  * * * * * * * * * * * * * 

'''

#PASCAL TRIANGLE
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(i):
        print('*',end=' ')
    for k in range(i):
        print(' ',end=' ')
    print()
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    for k in range(i):
        print(' ',end=' ')
    print()'''

'''
ENTER THE LIMIT :7

*   
* *     
* * *       
* * * *         
* * * * *           
* * * * * *             
* * * * * * * 
* * * * * *   
* * * * *     
* * * *       
* * *         
* *           
*             '''

#MIRROR IMAGE OF PASCAL TRIANGLE
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    print()
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(n-i):
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
* * * * * * * 
  * * * * * * 
    * * * * * 
      * * * * 
        * * * 
          * * 
            * 
'''

#MIRROR IMAGE OF PYRAMID
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print('*',end=' ')
    print()'''
'''
ENTER THE LIMIT :5
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        *
'''

#MIRROR IMAGE OF PYRAMID WITH NUMBERS
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print(i,end=' ')
    print()'''
'''
ENTER THE LIMIT :5
  1 1 1 1 1 1 1 
    2 2 2 2 2 
      3 3 3 
        4
'''

#increse by j
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print(k,end=' ')
    print()'''
'''
ENTER THE LIMIT :7
  0 1 2 3 4 5 6 7 8 9 10 
    0 1 2 3 4 5 6 7 8 
      0 1 2 3 4 5 6 
        0 1 2 3 4 
          0 1 2 
            0 
'''

#MIRROR IMAGE OF PYRAMID WITH ALPHABET
'''n=int(input('ENTER THE LIMIT :'))
for i in range(1,n):
    for j in range(i):
        print(' ',end=' ')
    for k in range(2*(n-i)-1):
        print(chr(64+i),end=' ')
    print()'''

'''
ENTER THE LIMIT :7
  A A A A A A A A A A A 
    B B B B B B B B B 
      C C C C C C C 
        D D D D D 
          E E E 
            F
'''

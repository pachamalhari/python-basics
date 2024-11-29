#STAR FULL BOX PATTERN
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()'''

'''
ENTER THE LIMIT :5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

#BOX
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''
ENTER THE LIMIT :7
* * * * * * * 
*           * 
*           * 
*           * 
*           * 
*           * 
* * * * * * * 
'''

#PLUS
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''
ENTER THE LIMIT :7
      *       
      *       
      *       
* * * * * * * 
      *       
      *       
      *
'''

#CROSS
'''n=int(input('ENTER THE LIMIT :'))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''
ENTER THE LIMIT :7
*           * 
  *       *   
    *   *     
      *       
    *   *     
  *       *   
*           * 
'''

#ARROW
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n): 
        if i==n//2 or j-i==n//2 or i+j==n+n//2-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''
ENTER THE LIMIT = 7
      *       
        *     
          *   
* * * * * * * 
          *   
        *     
      *     

'''

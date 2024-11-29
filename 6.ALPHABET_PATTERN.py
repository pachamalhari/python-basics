#A
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if (j==0 and i!=0) or (i==0 and j!=0 and j!=n-1) or (j==n-1 and i!=0) or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 5
  * * *   
*       * 
* * * * * 
*       * 
*       *   '''

#B
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if j==0 or (i==0 and j!=n-1) or (i==n-1 and j!=n-1) or (j==n-1 and i!=0 and i!=n-1 and i!=n//2) or (i==n//2 and j!=n-1) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 5
* * * *   
*       * 
* * * *   
*       * 
* * * *    '''

#C
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if (j==0 and i!=0 and i!=n-1) or (i==0 and j!=0) or (i==n-1 and j!=0):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 5
  * * * * 
*         
*         
*         
  * * * *    '''

#D
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if (i==0 and j!=n-1) or j==0 or(i==n-1 and j!=n-1) or (j==n-1 and i!=0 and i!=n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 5
* * * *   
*       * 
*       * 
*       * 
* * * *   '''

#E
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 5
* * * * * 
*         
* * * * * 
*         
* * * * *  '''

#F
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 5
* * * * * 
*         
* * * * * 
*         
*        ''' 


#G
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if (i==0 and j!=0 and j!=n-1) or (j==0 and i!=0 and i!=n-1) or (i==n-1 and j!=0 and j!=n-1) or (i==n//2 and j>=n//3) or (j==n-1 and i!=0 and i!=n-1 and i>=3):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
  * * * * *   
*             
*             
*   * * * * * 
*           * 
*           * 
  * * * * *   '''

#H
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if j==n-1 or j==0 or i==n//2 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 5
*       * 
*       * 
* * * * * 
*       * 
*       *  '''


#I
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() '''


'''ENTER THE LIMIT = 5
* * * * * 
    *     
    *     
    *     
* * * * *  '''


#J
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2 or (i==n-1 and j<=2) or (j==0 and i>=n//2): 
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 5
* * * * * 
    *     
*   *     
*   *     
* * *   ''' 

#K##
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if j==0 or i+j==3 or (j==i-(n//2) and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
*     *       
*   *         
* *           
*             
* *           
*   *         
*     *  '''     

#L
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
*             
*             
*             
*             
*             
*             
* * * * * * *  '''
#M
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and i<=2 and j<=2 ) or (i+j==n-1 and i<=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
*           * 
* *       * * 
*   *   *   * 
*     *     * 
*           * 
*           * 
*           * '''


#N
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if j==0 or j==i or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''ENTER THE LIMIT = 7
*           * 
* *         * 
*   *       * 
*     *     * 
*       *   * 
*         * * 
*           *  '''

#O
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if (i==0 and j!=0 and j!=n-1) or (j==0 and i!=0 and i!=n-1) or (j==n-1 and i!=0 and i!=n-1) or (i==n-1 and j!=0 and j!=n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
  * * * * *   
*           * 
*           * 
*           * 
*           * 
*           * 
  * * * * *    '''

#P
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if j==0 or (i==0 and j!=n-1) or (i==n//2 and j!=n-1) or (j==n-1 and i<n//2 and i!=0):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''
'''ENTER THE LIMIT = 7
* * * * * *   
*           * 
*           * 
* * * * * *   
*             
*             
*       '''      


#Q
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if (i==0 and j!=0 and j!=n-1) or (j==0 and i!=0 and i!=n-1) or (j==n-1 and i<=n//2 and i!=0) or (i==n-1 and j<=n//2 and j!=0) or (i==j and i>=2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
  * * * * *   
*           * 
*   *       * 
*     *     * 
*       *     
*         *   
  * * *     *  '''


#R
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if j==0 or (i==0 and j!=n-1) or (i==n//2 and j!=n-1) or (j==n-1 and i<n//2 and i!=0) or (i==j+2 and i>=n//3) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
* * * * * *   
*           * 
*           * 
* * * * * *   
*   *         
*     *       
*       *   '''
    
#S
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if (i==0 ) or (j==0 and i<=n//2 )or i==n//2 or i==n-1 or (j==n-1 and i>n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
* * * * * * * 
*             
*             
* * * * * * * 
            * 
            * 
* * * * * * *  '''

#T
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
* * * * * * * 
      *       
      *       
      *       
      *       
      *       
      *  '''     

#U
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if (j==0 and i!=n-1) or (i==n-1 and j!=0 and j!=n-1) or j==n-1 and i!=n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
*           * 
*           * 
*           * 
*           * 
*           * 
*           * 
  * * * * *   '''


#V
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if (i+j==n-1 and i<=n//2) or (i==j and i<=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
*           * 
  *       *   
    *   *     
      *       '''

#W
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i+j==n-1 and i>=n//2) or (i==j and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
*           * 
*           * 
*           * 
*     *     * 
*   *   *   * 
* *       * * 
*           * '''

#X
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
*           * 
  *       *   
    *   *     
      *       
    *   *     
  *       *   
*           * '''

#Y
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if (j==n//2 and i>=n//2) or (i==j and i<=n//2) or (i+j==n-1 and i<=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 7
*           * 
  *       *   
    *   *     
      *       
      *       
      *       
      *   '''

#Z
'''n=int(input('ENTER THE LIMIT = '))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''


'''ENTER THE LIMIT = 5
* * * * * 
      *   
    *     
  *       
* * * * *  '''

    

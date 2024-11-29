#1. Print the following pattern:
'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

'''for i in range(1,6):
    for j in range(6-i):
        print(j+1,end=' ')
    print()
for i in range(1,6):
    for j in range(i):
        print(j+1,end=' ')
    print()'''

'''1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 '''

#2. Print the following pattern:
'''
A B C D E
A B C D
A B C
A B
A
A B
A B C
A B C D
A B C D E
'''
'''for i in range(5):
    for j in range(5-i):
        print(chr(65+j),end=' ')
    print()
for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end=' ')
    print()'''
'''
A B C D E 
A B C D 
A B C 
A B 
A 
A 
A B 
A B C 
A B C D 
A B C D E 
'''

#3. Print the following pattern:
'''
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

'''for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
for i in range(1,6):
    for j in range(i):
        print(j+1,end=' ')
    print()'''
'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
'''
#4.
'''for i in range(5,0,-1):
    for j in range(i):
        print(i,end=' ')
    print()'''
''''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
'''
#5.
'''for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()'''
'''
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
'''


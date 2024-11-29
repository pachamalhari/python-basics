
def words(x):
    y=x.split()
    return len(y)

def length(x):
    print(len(x))

def vowels(x):
    c=0
    for i in x:
        
        if i in 'aeiouAEIOU':
            c+=1
    return c

           
    



    
#count of the tuple
'''my_tuple = (1, 2, 3, 1, 4, 1, 5)
count_of_1 = my_tuple.count(1)
print(count_of_1)''' 

#symmetric or not
'''user_input = input("Enter elements for the tuple, separated by spaces: ")
my_tuple = tuple(map(int, user_input.split()))
is_symmetric = my_tuple == my_tuple[::-1]
if is_symmetric:
    print("The tuple is symmetric.")
else:
    print("The tuple is not symmetric.")'''

#check prime number in given set
'''my_set = {2, 3, 5, 7, 10, 15}
num = 7
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime and num in my_set:
    print(f"{num} is a prime number and is present in the set.")
else:
    print(f"{num} is either not a prime number or not present in the set.")'''

#Remove duplicate in a list using set
'''my_list = [1, 2, 2, 3, 4, 4, 5, 6, 6]
unique_list = list(set(my_list))

print(unique_list)'''





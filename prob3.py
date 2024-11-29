# import math

# r=int(input("ENTER THE RADIUS :"))
# def are(r):
#     area=math.pi*r**2
#     perimeter=2*math.pi*r
#     print('AREA :',area,'PERIMETER :',perimeter)

# are(r)


# # ENTER THE RADIUS :5
# # AREA : 78.53981633974483 PERIMETER : 31.41592653589793

# math.

# import datetime

# x=datetime.datetime.now()
# print(x)
# print(dir(datetime))
#2024-10-24 13:12:57.832982
['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'time', 'timedelta', 'timezone', 'tzinfo']
''''''
# current_date =datetime.date.today()
# print(current_date)
# 2024-10-24
''''''
# d=datetime.date(2002,1,17)
# print(d)

# 2002-01-17

# from datetime import date
# today=date.today()
# print(today)

# 2024-10-24

# print('CURRENT YEAR:',today.year)
# print('CURRENT MONTH:',today.month)
# print('CURRENT DAY:',today.day)

# CURRENT YEAR: 2024
# CURRENT MONTH: 10
# CURRENT DAY: 24

from datetime import time
# time (hour = 0, minute = 0, second = 0)
a = time()
print (a)
# time (hour, minute and second)
b = time(11, 34, 56)
print(b)
# time (hour, minute and second)
c = time (hour = 11, minute = 34, second = 56)
print (c)
# time (hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print (d)

00:00:00
11:34:56
11:34:56
11:34:56.234566
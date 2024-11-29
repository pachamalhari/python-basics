import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='pshrfamily',
    database='hospital'                #use hospital
)

mycursor=mydb.cursor()

'''CREATE A DATABASE'''
# mycursor.execute('create database hospital')


'''SHOW DATABASES'''
# mycursor.execute('show databases')
# for i in mycursor:
#     print(i)


'''CREATE A TABLE as DOCTOR'''

# mycursor.execute('create table doctor (id int,name varchar(50),qualification varchar(50), salary int , age int)')

# mycursor.execute('show tables')
# for i in mycursor:
#     print(i)


'''insert'''
# mycursor.execute("insert into doctor values(01,'HARI','MBBS',100000,23)")
# mydb.commit()

'''Insert multiple values'''
# sql = 'insert into doctor(id,name,qualification,salary,age) values (%s,%s,%s,%s,%s)'
# val = [
#     ('2','RAHUL','BSC FORENSIC SCIENCE',50000,22),
#     ('3','SARASWATHY','PLUS TWO',20000,45),
#     ('4','PACHAMAL','PLUS ONE',100000,47)
# ]
# mycursor.executemany(sql, val)
# mydb.commit()
# print(mycursor.rowcount,'was inserted.')


'''Select from a table--- object to data'''
# mycursor.execute('select * from doctor')
# myresult = mycursor.fetchall()

# for x in myresult:
#     print(x)

'''using felchone() ---- single data'''
# mycursor.execute('select * from doctor')
# myresult = mycursor.fetchone()

# print(myresult)

'''select the filter'''
# sql='select * from doctor where age = 23'
# mycursor.execute(sql)
# myresult=mycursor.fetchall()

# for x in myresult:
#     print(x)

'''wildcard characters'''
# sql = 'select * from doctor where qualification like "%PLUS%"'
# mycursor.execute(sql)
# myresult=mycursor.fetchall()

# for x in myresult:
#     print(x)

'''DELETE record'''
# sql='delete from doctor where age="23"'
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount,"record(s) deleted")


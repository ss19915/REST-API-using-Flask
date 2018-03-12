import MySQLdb
file=open("data.txt","r")
data=file.read()
list=data.split("\r\n")
connection=MySQLdb.connect('localhost','root','1234','data')
cursor=connection.cursor()
pre=""
for i in list:
	t=i.split(',')
	if pre== t[0]:
		continue
	sql="insert into capital(country,capital) values('"+t[0].upper()+"','"+t[1].upper()+"')"
	cursor.execute(sql)
	pre=t[0]	
try:
	connection.commit()
	print "Operation Sucessful"
except:
	connection.rollback()
	print "Operation failed"
connection.close()	

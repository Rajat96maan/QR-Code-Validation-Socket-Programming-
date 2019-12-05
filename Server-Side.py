import mysql.connector as mysql # This module is used to connect python with MySQL database 
import socket
import sys 
import json

def server_program():
	HOST = '192.168.0.115' #this is your localhost
	PORT = 8888
	 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#socket.socket: must use to create a socket.
	#socket.AF_INET: Address Format, Internet = IP Addresses.
	#socket.SOCK_STREAM: two-way, connection-based byte streams.
	print('socket created')

	# Binding socket with post and host.
	try:
	    s.bind((HOST, PORT))
	except socket.error as err:
	    print('Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1])
	    sys.exit()
	 
	print('Socket Bind Success!')
	
	#listen(): This method sets up and start TCP listener. 
	s.listen(10)
	print ('Socket is now listening')
	 
	
	while True:
	    conn, addr = s.accept()
	    print ('Connect with ' + addr[0] + ':' + str(addr[1]))
	    df3 = conn.recv(1024).decode()# Here data will received from client port.
	    df3 = json.loads(df3)# Here data will decoded in json format.
	    print(df3)
	    
	    # This is mysql database which is connected with python.
	    #Here we need user,host,password and database name to connect with python
	    mydb1=mysql.connect(
		user = 'rajat',
	    passwd = 'rajat',
	    host = 'localhost',
	    database = 'myforum'
	    )

	    mycursor1=mydb1.cursor()
	    mycursor1.execute("SELECT * FROM form_simpleform WHERE id=1")# Its a mysql query which is selecting all fields from table where id is equals to one.
	    df2=mycursor1.fetchone() #fetchone() is used to fetch only one database.
	    print(list(df2))# When a row is fetch from database, it will print data in tuple.
	    # So we will convert it into list for comparison.

    	# Here we are doing the comparison of both list that is df3 to df2.
	    if df3 == (list(df2)):
	    	print('yes Data Exists')

	    	mydb2=mysql.connect(
			user = 'rajat',
		    passwd = 'rajat',
		    host = 'localhost',
		    database = 'after_validation'
		    )

	    	mycursor2 = mydb2.cursor()
	    	mycursor2.execute("SELECT * FROM android_display_data WHERE id=1")
	    	df4 = mycursor2.fetchone()
	    	df4 = list(df4)
	    	

	    	print("from connected user: " + str(df4))
	    	s.sendall(json.dumps(df4).encode('utf-8'))

	    else:
	    	print('Invalid Data')
	    	break

	    conn.close()
	    
	s.close()

if __name__ == '__main__':
    server_program()
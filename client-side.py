import socket
import sys
import datetime
import json
def client_prog():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.0.115', 8888)) #IP is the server IP
 
	for args in sys.argv:
		if args == '':
		    args = 'no args'
		else:
		    df1 = {'id':1,'Type_of_wallet':'Green', 'BLE_MAC_ID': '123456789', 'Bar_code': '456456', 'Version':2.0} #here we receive data from Android client
		    # for demo purpose we put the scan QR code data here for comparison.  
		    df3 = list(df1.values())#Converting the Dictionary into list and the use of values() function will gives only values of keys.
		    s.sendall(json.dumps(df3).encode('utf-8'))
		    print('Data is sent to the server!!')

		    df4=s.recv(1024).decode('utf-8')
		    df4 = json.loads(df4)
		    print(df4)
		    print('Data received from server!!')			

if __name__ == '__main__':
	client_prog()




# for QR CODE PROJECT
#The usual way is to convert the datetime to a str. 
#You can do that using by using a custom encoder in the json.dumps 
#like json.dumps(dict, default=myconverter) 
#and the decode in the other side,
 #and convert the datetime object back from str

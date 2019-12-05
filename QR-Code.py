import pyqrcode 
from pyqrcode import QRCode 
  
  
# String which represent the QR code 
s = {'id':1,'Type_of_wallet':'Green', 'BLE_MAC_ID': '123456789', 'Bar_code': '456456', 'Version':2.0}

url=str(s).encode('utf-8')

url1=pyqrcode.create(url)

url1.svg("myqr112.svg", scale = 8) 
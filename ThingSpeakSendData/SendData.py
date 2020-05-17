import sys
import urllib.request
from time import sleep

myAPI='writeAPIKey'
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI

data1=1.2323
data2=6765.2342
data3=0.34324
data4=45.3423
data5=23.0

response = urllib.request.urlopen(baseURL + '&field1=%s&field2=%s&field3=%s&field4=%s&field5=%s' % (data1,data2,data3,data4,data5))
print (response.read())
			# Closing the connection
response.close()




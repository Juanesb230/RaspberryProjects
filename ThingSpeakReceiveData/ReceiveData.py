import xml.etree.ElementTree as ET
import sys
import urllib.request

myAPI = 'readAPIKey'
baseURL1 = 'https://api.thingspeak.com/channels/826316/fields/1.xml?api_key=%s' % myAPI
baseURL2 = 'https://api.thingspeak.com/channels/826316/fields/2.xml?api_key=%s' % myAPI
baseURL3 = 'https://api.thingspeak.com/channels/826316/fields/3.xml?api_key=%s' % myAPI
baseURL4 = 'https://api.thingspeak.com/channels/826316/fields/4.xml?api_key=%s' % myAPI
baseURL5 = 'https://api.thingspeak.com/channels/826316/fields/5.xml?api_key=%s' % myAPI
baseURL = [baseURL1, baseURL2, baseURL3, baseURL4, baseURL5]
fields = ['field1', 'field2', 'field3', 'field4', 'field5']
i = 0
data = [0, 0, 0, 0, 0]

for index, URL in enumerate(baseURL):
  conn = urllib.request.urlopen(URL + '&results=1')
  xml_data = conn.read()
  conn.close()
  doc = ET.fromstring(xml_data)
  feeds = doc.find('feeds')
  feed = feeds.find('feed')
  field = feed.find(fields[index]).text
  data[index] = float(field)

print (data)
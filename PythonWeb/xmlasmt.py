import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'


address = input('Enter location: ')
    # if len(address) < 1: break

    #url = serviceurl + urllib.parse.urlencode({'address': address})
print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read()
#print('Retrieved', len(data), 'characters')
#print(data.decode())
tree = ET.fromstring(data)
sumc = tree.findall('comments/comment')
#print(sumc)
sumt = 0
for child in sumc:
    c = child.find('count').text
    sumt = sumt + int(c)
print(sumt)


    # results = tree.findall('result')
    # lat = results[0].find('geometry').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text
    #
    # print('lat', lat, 'lng', lng)
    # print(location)

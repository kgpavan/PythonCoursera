import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://python-data.dr-chuck.net/geojson?sensor=false&'

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode(
        {'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    # if not js or 'status' not in js or js['status'] != 'OK':
    #     print('==== Failure To Retrieve ====')
    #     print(data)
    #     continue

    #print(json.dumps(js, indent=4))

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    place_id = js["results"][0]["place_id"]
    print('lat', lat, 'lng', lng, 'place_id',place_id)
    location = js['results'][0]['formatted_address']
    print(location)

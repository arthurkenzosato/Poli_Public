import urllib, urllib2
import base64
import time
import sys

if __name__ == '__main__':
    page = 'http://argus-adrianodennanni.c9.io/send_snap'
    with open("/home/ricardo/Documents/fig3.png", "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read())
    raw_params = {'timestamp': int(time.time()), 'image': encoded_image, 'house_id': 3}
    params = urllib.urlencode(raw_params)
    request = urllib2.Request(page, params)
    request.add_header("Content-type", "application/x-www-form-urlencoded; charset=UTF-8")
    try: 
    	page = urllib2.urlopen(request)
    except urllib2.HTTPError as e:
		error_message = e.read()
		print error_message
    print 'Sent!'
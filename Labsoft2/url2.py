import urllib
url = "http://argus-adrianodennanni.c9.io/"
values = {'open':'0' ,
          'sensor_id' : '1','house_id' : '1'
          }
url_values = urllib.urlencode(values)
url_full = url + '?' + url_values

response = urllib.urlopen(url_full).read()
print response
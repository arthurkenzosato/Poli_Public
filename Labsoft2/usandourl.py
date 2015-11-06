import urllib2
import urllib

url = 'http://http://argus-adrianodennanni.c9.io/'
values = {'open':'0' ,
          'sensor_id' : '1','house_id' : '1'
          }
url_values = urllib.urlencode(values)
full_url = url + '?' + url_values
print(full_url)

#data = urllib.urlencode(values)
#req = urllib2.Request(full_url)


response = urllib2.urlopen(full_url)
#the_page = response.read()
#print(the_page)
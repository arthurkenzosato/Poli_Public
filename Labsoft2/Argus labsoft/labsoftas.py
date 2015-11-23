import urllib
import thread
import RPi.GPIO as GPIO
import time

#house_id = 1



url = "http://argus-adrianodennanni.c9.io/sensor_update"

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


window1 = 2
window2 = 3
door = 4

GPIO.setup(window1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(window2, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(door, GPIO.IN, GPIO.PUD_UP)



#main

current_window1 = GPIO.input(window1)
current_window2 = GPIO.input(window2)
current_door = GPIO.input(door)



		
#envia pro servidor e printa a resposta
def envia_server(idsensor,estadosensor):
	global url
	values = {'open':estadosensor ,
          'sensor_id' : idsensor ,'house_id' : '1'
          }
    
    	url_values = urllib.urlencode(values)
	url_full = url + '?' + url_values
	print url_full
	response = urllib.urlopen(url_full).read()
	print response
		

#Funcao de leitura dos sensores, envia json se algo mudar
def my_callback(event):

	global current_window1
	global current_window2
	global current_door
	global window1
	global window2
	global door
	

	if GPIO.input(window1) != current_window1:
		if GPIO.input(window1) == True:
			print("Abriram a janela1")
			envia_server(1,0)
		else :
			print("Fecharam a janela1")
			envia_server(1,1)
		current_window1 = GPIO.input(window1) #atualiza


	if GPIO.input(window2) != current_window2:
		if GPIO.input(window2) == True:
			print("Abriram a janela2")
			envia_server(2,0)
		else :
			print("Fecharam a janela2")
			envia_server(2,1)			
		current_window2 = GPIO.input(window2) #atualiza

	if GPIO.input(door) != current_door:
		if GPIO.input(door) == True:
			print("Abriram a porta")
			envia_server(0,0)
		else :
			print("Fecharam a porta")
			envia_server(0,1)
		current_door = GPIO.input(door)	#atualiza


GPIO.add_event_detect(window1, GPIO.RISING, callback=my_callback) 
#GPIO.add_event_detect(window2, GPIO.RISING, callback=my_callback) 
#GPIO.add_event_detect(door, GPIO.RISING, callback=my_callback)



# def dumpJson(house_id,mode,sensor1, sensor2, sensor3):
#	data = {'house_id':house_id,'mode':mode,'sensor1':sensor1,'sensor2':sensor2,'sensor3':sensor3}
#	json_data = json.dumps(data)





while True:
	pass
	input
	






GPIO.cleanup()

print("Fabyfaby")


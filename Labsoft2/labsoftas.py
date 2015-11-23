import urllib
import thread
import RPi.GPIO as GPIO
import time
import urllib2
import base64
import sys

#house_id = 1



url = "http://argus-adrianodennanni.c9.io/"


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
def send_up_sensor(idsensor,estadosensor):
	global url
	url_sensor = url + "sensor_update/"
	values = {'open':estadosensor ,
          'sensor_id' : idsensor ,'house_id' : '1'
          }
    
    	url_values = urllib.urlencode(values)
	url_full = url_sensor + '?' + url_values
	print url_full
	response = urllib.urlopen(url_full).read()
	print response
	

#pede para mudar o estado do alarm, PAREM DE MUDAR O NOME DAS COISAS QUE EU COLOCO
def send_activate_alarm():
	global url
	url_alarm_switch = url + "alarm_switch"
	print url_alarm_switch 
	response = urllib.urlopen(url_alarm_switch).read()
	print response

#Funcao de leitura do input no teclado
def read_input(keyboard_input):
	if keyboard_input == "/123":
		send_activate_alarm()



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
			send_up_sensor(1,0)
		else :
			print("Fecharam a janela1")
			send_up_sensor(1,1)
		current_window1 = GPIO.input(window1) #atualiza


	if GPIO.input(window2) != current_window2:
		if GPIO.input(window2) == True:
			print("Abriram a janela2")
			send_up_sensor(2,0)
		else :
			print("Fecharam a janela2")
			send_up_sensor(2,1)			
		current_window2 = GPIO.input(window2) #atualiza

	if GPIO.input(door) != current_door:
		if GPIO.input(door) == True:
			print("Abriram a porta")
			send_up_sensor(0,0)
		else :
			print("Fecharam a porta")
			send_up_sensor(0,1)
		current_door = GPIO.input(door)	#atualiza


GPIO.add_event_detect(window1, GPIO.RISING, callback=my_callback) 
#GPIO.add_event_detect(window2, GPIO.RISING, callback=my_callback) 
#GPIO.add_event_detect(door, GPIO.RISING, callback=my_callback)



# def dumpJson(house_id,mode,sensor1, sensor2, sensor3):
#	data = {'house_id':house_id,'mode':mode,'sensor1':sensor1,'sensor2':sensor2,'sensor3':sensor3}
#	json_data = json.dumps(data)





#codigo do frances
def check_password(user_input):
	try :
		f = open('password', 'r')
		password = f.read()
		if user_input == password :
			return True
		else :
			return False
	except IOError:
		f = open('password', 'w')
		f.write('1234')
		check_password(user_input)


def change_password():
	timeout = 20
	entry = getpass.getpass( "Enter a new password : ")
	check_entry = getpass.getpass( "Please enter a second time : ")
	if entry == check_entry:
		f = open('password', 'w')
		f.write(entry)
		print "Change password successful"
	else: 
		print "Change password failed (password different)..."



def log_out():
	global user_auth
	user_auth = False
	print "Logout"

def start_mode1():
	print "Mode 1 started"

def start_mode2():
	print "Mode 2 started"

def start_mode3():
	print "Mode 3 started"
	
def start_mode4():
	print "Mode 4 started"


def select_mode(user_input):
	if user_input == '000':
		change_password()
	elif user_input == '100' :
		log_out()
	elif user_input == '1' :
		start_mode1()
	elif user_input == '2' :
		start_mode2()
	elif user_input == '3' :
		start_mode3()
	elif user_input == '4' :
		start_mode4()

while True:
	keyboard_input = raw_input("Please enter your mode")
	select_mode(keyboard_input)
		
'''
Codigo do broco

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
'''





GPIO.cleanup()

print("Fabyfaby")



from multiprocessing import Queue,Process,Pipe,Lock,Manager
import RPi.GPIO as GPIO
import time


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



def readKeyboard(event):
	leitura = int(input())
	if(leitura == 1):
		print("modo1 ativado")
		
	elif(leitura==2):
		print("insira senha panico")
		
		

#Função de leitura dos sensores, envia json se algo mudar
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
		else :
			print("Fecharam a janela1")
		current_window1 = GPIO.input(window1)


	if GPIO.input(window2) != current_window2:
		if GPIO.input(window2) == True:
			print("Abriram a janela2")
		else :
			print("Fecharam a janela2")

		current_window2 = GPIO.input(window2)

	if GPIO.input(door) != current_door:
		if GPIO.input(door) == True:
			print("Abriram a porta")
		else :
			print("Fecharam a porta")

		current_door = GPIO.input(door)	


#GPIO.add_event_detect(window1, GPIO.RISING, callback=my_callback) 
#GPIO.add_event_detect(window2, GPIO.RISING, callback=my_callback) 
#GPIO.add_event_detect(door, GPIO.RISING, callback=my_callback)

while True:
	#q = Queue()
	readKey = Process(target=readKeyboard,args=())
	readKey.start()
	#data=q.get()
	#print (data)
	readKey.join()

	
	time.sleep(1)

# def dumpJson(house_id,mode,sensor1, sensor2, sensor3):
#	data = {'house_id':house_id,'mode':mode,'sensor1':sensor1,'sensor2':sensor2,'sensor3':sensor3}
#	json_data = json.dumps(data)






	






GPIO.cleanup()

print("Fabyfaby")



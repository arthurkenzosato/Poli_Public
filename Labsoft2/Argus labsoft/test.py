import urllib
import time
import getpass
import sys

from select import select


"""
import socket, ssl, pprint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Require a certificate from the server. We used a self-signed certificate
# so here ca_certs must be the server certificate itself.
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="ssl_cert",
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('192.168.0.15', 10023))

print repr(ssl_sock.getpeername())
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())

ssl_sock.write("boo!")

if False: # from the Python 2.7.3 docs
    # Set a simple HTTP request -- use httplib in actual code.
    ssl_sock.write(""GET / HTTP/1.0\r
    Host: www.verisign.com\n\n"")

    # Read a chunk of data.  Will not necessarily
    # read all the data returned by the server.
    data = ssl_sock.read()

    # note that closing the SSLSocket will also close the underlying socket
    ssl_sock.close()
"""







user_auth = False



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
	if user_auth != True :
		entry = getpass.getpass("Enter your login password :")
		if check_password(entry) == True :
			user_auth = True
			print "Login successful"
	else :
		timeout = 20
		print "Choose your mode : "
		rlist, _, _ = select([sys.stdin], [], [], timeout)
		if rlist:
			entry = sys.stdin.readline().rstrip('\n')
			select_mode(entry)
		else:
			log_out()
			print "No input. Logout..."
		
		

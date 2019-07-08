import string
import time
from Read import getUser, getMessage
from Socket import openSocket, sendMessage
from Initialize import joinRoom

s = openSocket()
joinRoom(s)
readbuffer = ""

while True:
    readbuffer = readbuffer + s.recv(1024)
    temp = string.split(readbuffer, "\n")
    readbuffer = temp.pop()
    streamStart = time.time
    messageString = "The time you started was" + streamStart
    sendMessage(s, "hello")
		#for line in temp:
			#print(line)
			#if "PING" in line:
				#s.send(line.replace("PING", "PONG"))
				#break
			#user = getUser(line)
			#message = getMessage(line)
			#print user + " typed :" + message
			#if "You Suck" in message:
				#sendMessage(s, "No, you suck!")
				#break
			

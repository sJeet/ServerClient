# Server Code
 
host="127.0.0.1"                # Set the server address to variable host
port=4446                       # Sets the variable port to 4446
from socket import *            # Imports socket module
 
s=socket(AF_INET, SOCK_STREAM)
 
s.bind((host,port))             # Binds the socket.
s.listen(1)                     # Sets socket to listening state with a  queue
                                
print "Listening for connections.. "
 
q,addr=s.accept()               # Accepts incoming request from client and returns
                                
data=raw_input("Enter data to be send:  ")  # Data to be send is stored in variable data from
                                
q.send(data)                    # Sends data to client
 
s.close()
 
# End of code

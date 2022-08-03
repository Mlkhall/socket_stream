import time
import random
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    message = ', '.join(map(str, random.sample(range(10, 30), 5)))
    print(message.encode('utf-8'))
    socket.send_multipart([b"", message.encode('utf-8')])

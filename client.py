import zmq
context = zmq.Context()
print("Connecting to hello world server")
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
while True:
    print("Sending request %s")
    cb, hb = socket.recv_multipart()

    print(f"Received reply {cb.decode('utf-8'), hb.decode('utf-8')}")

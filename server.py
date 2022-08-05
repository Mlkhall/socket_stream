import base64
import random
import time

import cv2
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5555")
# Открывает камеру для захвата видео
# В параметрах передается id  устройства (для работы по умолчанию 0)
camera = cv2.VideoCapture(0)

while True:
    try:
        #  Wait for next request from client

        #  Do some 'work'
        time.sleep(1)
        #  Send reply back to client
        message = ', '.join(map(str, random.sample(range(10, 30), 5)))
        print(message.encode('utf-8'))
        socket.send_multipart([b"", message.encode('utf-8')])
        # Захватывает, декодирует и возвращает кадр
        ret, frame = camera.read()
        frame = cv2.resize(frame, (640, 480))
        # Кодирует изображение в буфер памяти
        encoded, buf = cv2.imencode('.jpg', frame)
        # Кодирование
        image = base64.b64encode(buf)
        socket.send(image)
    except KeyboardInterrupt:
        # Закрывает видеофайл или устройство захвата
        camera.release()
        # Закрывает окна
        cv2.destroyAllWindows()
        break

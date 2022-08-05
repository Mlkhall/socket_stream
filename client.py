import base64

import cv2
import numpy as np
import zmq

context = zmq.Context()
print("Connecting to hello world server")
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")
socket.setsockopt_string(zmq.SUBSCRIBE, '')


while True:
    try:
        print("Sending request %s")
        cb, hb = socket.recv_multipart()

        print(f"Received reply {cb.decode('utf-8'), hb.decode('utf-8')}")
        image_string = socket.recv_string()
        # декодирует переданный файл
        raw_image = base64.b64decode(image_string)
        # Интерпретирует буфер как одномерный массив
        image = np.frombuffer(raw_image, dtype=np.uint8)
        # Считывает изображение из буфера
        frame = cv2.imdecode(image, 1)
        # Добавление изображения в окно
        cv2.imshow("frame", frame)
        # Остановка изображения от быстрого исчезновения
        cv2.waitKey(1)
    except KeyboardInterrupt:
        # Закрывает окна
        cv2.destroyAllWindows()
        break

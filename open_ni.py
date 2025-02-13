import cv2
import openni

# Инициализация OpenNI
openni.initialize()

# Создание устройства
device = openni.Device.open_any()

# Создание потоков
depth_stream = openni.VideoStream(device, openni.SENSOR_DEPTH)
depth_stream.start()

# Захват и отображение глубины
try:
    while True:
        frame = depth_stream.read_frame()
        depth_data = frame.get_buffer_as_uint16()

        # Обработка данных глубины (например, преобразование в изображение)
        depth_image = np.array(depth_data).reshape((frame.height, frame.width))

        # Отображение изображения глубины
        cv2.imshow('image.jpg', depth_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Освобождение ресурсов
    depth_stream.stop()
    device.close()
    openni.shutdown()
    cv2.destroyAllWindows()

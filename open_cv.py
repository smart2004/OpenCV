import cv2

image = cv2.imread('image.jpg')  # upload image

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # conversion into gray

cv2.imshow('Original Image', image)  # original / gray image reflection
cv2.imshow('Gray Image', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


# OpenCV[Open Source Computer Vision Library] — это библиотека для компьютерного зрения и обработки изображений. 
# Вот пример кода, который загружает изображение, 
# преобразует его в оттенки серого и отображает результат:

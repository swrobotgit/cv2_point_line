import cv2
import random

# Создаем изображение размером 800x800 пикселей
image = cv2.imread('image.jpg')

# Генерируем 10 случайных центров для кругов
q_circle = random.randint(10, 20)
centers = []
for _ in range(q_circle):
    x = random.randint(50, 750)
    y = random.randint(50, 750)
    center = (x, y)
    centers.append(center)


# Рисуем круги с центрами
for center in centers:
    cv2.circle(image, center, 10, (0, 0, 255), -1) # рисуем круг радиусом 30 пикселей

print(centers)
# Соединяем круги линиями
for i in range(len(centers) - 1):
    print(centers[i])
    cv2.line(image, centers[i], centers[i+1], (0, 0, 255), 1)

# Соединяем последний и первый круг
# cv2.line(image, centers[-1], centers[0], (0, 0, 255), 1)

# Показываем изображение в окне
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

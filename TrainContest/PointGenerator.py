from math import pi, cos, sin, sqrt
from random import uniform
import sys

def generate1():
    a = uniform(0, 1)
    b = uniform(0, 1)
    return f"{a * cos(2 * pi * b)} {a * sin(2 * pi * b)}"


def generate2():
    while True:
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        if x ** 2 + y ** 2 > 1:
            continue
        return f"{x} {y}"


def generate_train_points():
    data = []
    string = ""
    for i in range(100):
        for j in range(1000):
            if i % 2 == 0:
                string += generate1() + (" " if j != 999 else "")
            else:
                string += generate2() + (" " if j != 999 else "")

        data.append(string)

    return data

train_points = generate_train_points()

def classify_set(str_points):


    distances = [sqrt(x**2 + y**2) for x, y in points]

    # Вычисляем среднее расстояние
    mean_distance = sum(distances) / len(distances)

    # Используем порог для классификации генератора
    threshold = 0.7
    if mean_distance < threshold:
        return 1
    else:
        return 2



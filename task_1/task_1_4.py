import math

v0 = float(input("Введіть початкову швидкість (м/с): "))
angle = float(input("Введіть кут (градуси): "))

g = 9.81
rad = math.radians(angle)

max_h = (v0 * math.sin(rad)) ** 2 / (2 * g)
print(max_h)

total_t = 2 * v0 * math.sin(rad) / g

t = 0
while t <= total_t:
    h = v0 * math.sin(rad) * t - 0.5 * g * t ** 2
    print(t, h)
    t += 1
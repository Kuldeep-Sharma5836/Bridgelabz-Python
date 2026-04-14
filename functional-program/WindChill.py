import math

t = float(input("Enter temperature: "))
v = float(input("Enter wind speed: "))

if abs(t) > 50 or v < 3 or v > 120:
    print("Invalid input")
else:
    w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
    print("Wind Chill =", w)

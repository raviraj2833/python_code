import random
import math

B = random.randint(1, 20)
C = 2
A = B * C

print(f"Quadratic Equation: {A}x² + {B}x + {C} = 0")
D = B**2 - 4*A*C

if D > 0:
    root1 = (-B + math.sqrt(D)) / (2*A)
    root2 = (-B - math.sqrt(D)) / (2*A)
    print(f"Two Real Solutions: x1 = {root1}, x2 = {root2}")
elif D == 0:
    root = -B / (2*A)
    print(f"One Real Solution: x = {root}")
else:
    real = -B / (2*A)
    imag = math.sqrt(-D) / (2*A)
    print(f"Two Complex Solutions: x1 = {real} + {imag}i, x2 = {real} - {imag}i")

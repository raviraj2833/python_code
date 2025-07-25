import math
A = float(input("Enter value for A: "))
B = 3 * A
C = A - 3
print(f"Quadratic Equation: {A}x² + {B}x + {C} = 0")

D = B**2 - 4*A*C
if D > 0:
    root1 = (-B + math.sqrt(D)) / (2*A)
    root2 = (-B - math.sqrt(D)) / (2*A)
    print(f"Two Real Roots: x1 = {root1}, x2 = {root2}")
elif D == 0:
    root = -B / (2*A)
    print(f"One Real Root: x = {root}")
else:
    real_part = -B / (2*A)
    imaginary_part = math.sqrt(-D) / (2*A)
    print(f"Two Complex Roots: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")

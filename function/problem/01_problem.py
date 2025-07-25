def tempConvert(n):
    if n==0:
        return 32
    return (n*9/5) +32

n=int(input("Enter degree in celcius:"))
print(f"Temp in fahrenheit at {n}°C is  {tempConvert(n)}°F")
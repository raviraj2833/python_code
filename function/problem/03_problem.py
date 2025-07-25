def sumN(n):
    if n==1:
        return 1
    return sumN(n-1)+n

n=int(input("Enter the number: "))
print(f"Sum of first {n} natural number = {sumN(n)}")

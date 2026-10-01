# Write a Python program to print the multiplication table of a given number.

def multi (n):
    for i in range(1, 11):
        print(f"{n}x{i}={n*i}")

multi(5)
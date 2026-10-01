# write a program using function to convert temperature from fahrenheit to celsius

def f_to_c():
    f =int(input("Enter temperature in F: "))
    c = 5*(f - 32) / 9
    return c
print(f_to_c())

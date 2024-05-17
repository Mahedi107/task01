def add(x, y):
    result = x + y
    # checking if inputs are validated
    print(type(x))
    print(type(y))
    return result

result = add(2, 3)

print(f"System result is {result}")


def multiply(x, y):
    result = x * y
    return result

mult = multiply(2,3) 
print(f"mutliply result is {mult}")
def add(x, y):
    result = x + y
    # checking if inputs are validated
    print(type(x))
    print(type(y))
    return result

result = add(2, 3)

print(f"System result is {result}")
# Declaring the function that accepts two ints
def multiply(x: int, y: int) -> None:
    result: int = x * y
    print("x value:", x)
    print("y value:", y)
    print(result)

# To call it
multiply(4, 5)  # the 4 is the x value and 5 is the y value
# output:
# x value: 4
# y value: 5
# 20   
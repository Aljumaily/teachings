def multiply(x: int, y: int) -> int:
  result: int = x * y
  return result

# To call it, all are valid but it depends on what you are doing:
multiply(4, 5)             # call the function but don't use the value returned
print(multiply(4, 5))      # call the function and print the value returned
value:int = multiply(4, 5) # store the value returned in a variable
print(value)               # print the value of the variable
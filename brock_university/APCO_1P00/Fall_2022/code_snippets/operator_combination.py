x: int = 0
while (x >= 0 and x <= 10) or x == 11 or x < 0:
    print(x, end=" ")
    x = x + 1
# output: 0 1 2 3 4 5 6 7 8 9 10 11
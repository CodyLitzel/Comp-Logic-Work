def greater_than(x, y):
    if x > y:
        return True
    else:
        return False
a = 10
b = 6
results = greater_than(a, b)
print("The statement " + str(a) + " is greater than " + str(b) + " is " + str(results).lower())

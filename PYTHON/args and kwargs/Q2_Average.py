def average(*args):
    total = sum(args)
    count = len(args)
    if count == 0:
        return 0
    return total / count
print(average(10, 20))
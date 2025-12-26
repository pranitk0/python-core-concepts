count = 0  
def increment():
    global count
    count += 1
    print("Inside function:", count)
increment()
increment()
print("Outside function:", count)

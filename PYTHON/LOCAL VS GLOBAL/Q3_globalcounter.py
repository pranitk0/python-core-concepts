counter = 0   
def increment():
    global counter
    counter += 1
    print("Counter inside function:", counter)
increment()
increment()
increment()
print("Counter outside function:", counter)

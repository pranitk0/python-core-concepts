count = 0  
def increment():
    global count      
    count += 1
    print("Count inside function:", count)
increment()
increment()
increment()
increment()
print("Final count:", count)

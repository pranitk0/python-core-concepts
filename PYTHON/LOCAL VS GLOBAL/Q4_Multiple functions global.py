count = 0  
def add_one():
    global count       
    count += 1
    print("After add_one:", count)

def subtract_one():
    global count
    count -= 1
    print("After subtract_one:", count)

add_one()       
add_one()       
subtract_one()  

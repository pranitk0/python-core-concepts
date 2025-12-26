count = 0  

def outer():
    def inner():
        global count   
        count += 1
        print("Inner function count:", count)
    
    inner()

outer()
print("Global count after outer call:", count)

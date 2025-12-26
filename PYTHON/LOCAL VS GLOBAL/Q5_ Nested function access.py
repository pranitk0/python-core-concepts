def outer():
    x = 10   

    def inner():
        print("Inner accessing outer x:", x)  

    inner()

outer()

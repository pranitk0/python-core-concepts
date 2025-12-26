#Q1
def my_function():
    x = 1 
    print(x)
my_function()    

#Q2
x=22
def my_function():
    print(x)
my_function()

#Q3
y=11
def global_local():
    y= 12
    def inner():
        print("local function:",y)
    inner()
global_local()
print("global:",y)

#Q4
x=10
def my_function():
    global x
    x=20
    print(x)
my_function() 

#Q5
x=100
def my_function():
    x = 200
    print(x)
my_function()
print(x)

#Q6
num=11
num2=12
def my_function():
    global num , num2
    num = 200
    num2 = 100
my_function()
print(num)
print(num2)

#Q7
x=10 
def my_function():
    global x
    x = x + 10 
my_function()    
print(x)

x=200 
def my_function(value):
    value = value + 10 
    return value
x = my_function(x)    
print(x)    
    
#Q8
"""def my_function():
    x = 200
    print(x)
my_function()
print(x)"""

#Q9

def outer ():
    x = 10
    def inner():
         print(x)
    inner()
outer()    

#Q10
counter = 10 
def my_counter():
    global counter
    counter = counter + 1
my_counter()
print(counter)








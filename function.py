def my_function():
  print("Hello from a function")

my_function()

def adding():
    x=2
    b=4
    print(x+b)
    
adding()


#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
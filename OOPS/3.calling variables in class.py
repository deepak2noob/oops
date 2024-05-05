class MyClass:
    def __init__(self, value):
        self.value = value

    def display_value(self):
        # Creating a method variable
        method_variable = 20
        print("Method variable:", method_variable)


# Creating an instance of MyClass
obj = MyClass(10)

# Accessing constructor variable 
print("Constructor variable accessed using instance:", obj.value)


# Calling the method variable
obj.display_value()

#--------------------------------------------------------------------


#calling constructor variable in method of same class
class Myclass2:
    def __init__(self,value): #constructor
        self.value = value
    def method(self):
        print("constructor variable is",self.value) 
                  # you cant write value.. it will give u error

obj2=Myclass2("bruh")  
print(obj2.method())      

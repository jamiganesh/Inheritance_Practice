class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # <-- This is where we use the super() function
        print("Hello from Child")

c = Child()
c.greet()


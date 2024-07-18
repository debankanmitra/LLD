class Test:
    x = 10 # class object variable
    def __init__(self, name, age): # to make instance object variable we use, __init__ constructor
        self.name = name
        self.age = age

    def display(self): # to make instance method first argument will be self
        print(self.name, self.age)

    @staticmethod
    def hello(): # static method
        print("hello", Test.x)

    @classmethod
    def hi(cls): # class method
        print("hi")

t = Test("John", 36) # __init__(t1), so self = t1 
t.display()
Test.hello()
t.hello()

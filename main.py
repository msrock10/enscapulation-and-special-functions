class myclass:

    __privateVar = 27;

    def __prevMeth(self):
        print("I'm inside  myclass")

    def hello(self):
        (print("print variable value",myclass.__privateVar))

foo = myclass()
foo.hello()

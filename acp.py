class reverse:
    def __init__(self,data):
        self.data = data
    
    def reverse(self):
        return self.data[::-1]
        
a = input("Enter a string: ")
r=reverse(a)
print(r.reverse())
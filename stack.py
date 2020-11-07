class stack:
    def __init__(self):
        self.stack = []

# using list append method to add elements to the list 
     
    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True

        else:
            return False

# returning the top most element of the stack 
    
    def top_most(self):
        return self.stack[-1]

# using list pop method to remove the last elements from the list

    def pop_the_last(self):
        if len(self.stack) <=0:
            return ("no elements in the stack")
        else:
            return self.stack.pop()

Astack = stack()
Astack.add("mon")
Astack.add("tue")
Astack.add("wed")


print(Astack.top_most())
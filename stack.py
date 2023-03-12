class Stack:
    def __init__(self):
        self.stack = []

    def stackUp(self, item):
        self.stack.append(item)

    def unstack(self):
        if len(self.stack) > 0:
            self.stack.pop()
    
    def showStack(self):
        print(self.stack)
    
    def emptyStack(self):
        if len(self.stack) < 1:
            return True
        else:
            return False
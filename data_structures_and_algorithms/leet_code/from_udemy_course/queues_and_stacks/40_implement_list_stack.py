# class Stack:
#     def __init__(self, value):
#         self.stack_list = [] 


class Stack:
    def __init__(self, value):
        self.stack_list = [value] 

stack = Stack(10)
print(stack.stack_list)

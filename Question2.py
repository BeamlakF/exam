def create_new_stack():
    stack=[]
    return stack
def is_empty(stack):
    return len(stack)==0
def push(stack, item):
    stack.append(item)
    print('pushed item:' + item)
def pop(stack):
    if is_empty(stack):
        return("Stack is empty") 
    else:
        return stack.pop()
#USAGE 
stack=create_new_stack()
push(stack,str(1))
push(stack,str(2))
print('popped items:' + pop(stack))      
print('After removing an element:' + str(stack))
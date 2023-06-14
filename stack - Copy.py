def stack():
    stack=[]
    return stack
def isempty(stack):
    return stack==0

def push(stack,item):
    stack.append(item)
    print("item:"+item)

def pop(stack):
    return stack.pop()

stack=stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
print("append item:"+pop(stack))
print("stack after poping an elements:"+str(stack))






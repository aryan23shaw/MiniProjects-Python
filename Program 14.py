stack = []

def push(stack, value):
    stack.append(value)
    print(f"Pushed {value} to stack.")

def pop(stack):
    if stack:
        value = stack.pop()
        print(f"Popped {value} from stack.")
    else:
        print("Stack is empty.")

push(stack, 10)
pop(stack)

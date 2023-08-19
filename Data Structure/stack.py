stack = []
  
# append() function to push
# element in the stack
stack.append('g')
stack.append('f')
stack.append('g')
  
print('Initial stack')
print(stack)         #['g', 'f', 'g']
  
# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())  #g 
print(stack.pop())  #f
print(stack.pop())  #g
  
print('\nStack after elements are popped:')
print(stack)    #[]
  
# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty
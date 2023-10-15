import sys

input=sys.stdin.readline

N = int(input())

stack = []

for i in range(N):
  k = list(input().split())
  if len(k) == 2:
    stack.append(int(k[1]))
  else:
    if k[0] == 'pop':
      if len(stack) == 0:
        print(-1)
      else:
        print(stack.pop())
    elif k[0] == 'size':
      print(len(stack))
    elif k[0] == 'empty':
      if len(stack) == 0:
        print(1)
      else:
        print(0)
    else:
      if len(stack) == 0:
        print(-1)
      else:
        print(stack[len(stack)-1])
      
    
  
    
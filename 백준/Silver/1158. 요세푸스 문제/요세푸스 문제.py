from collections import deque

n, k = map(int,input().split())

d = deque()

result = []

for i in range(n):
  d.append(i+1)

while d:
  # k-1까지 맨 앞을 뒤로 보내준다
  for _ in range(k-1):
    d.append(d.popleft())
  # 맨 왼쪽을 pop해서 result에 넣어준다.
  result.append(d.popleft())

print(str(result).replace('[','<').replace(']','>'))
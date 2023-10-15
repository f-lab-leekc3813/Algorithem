N = int(input())

people = []
result = ''

for _ in range(N):
  x, y = map(int, input().split())
  people.append([x,y])

for i in range(len(people)):
  now_count = 0
  for j in range(len(people)):
    if i == j :
      continue
    if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
      now_count += 1
  result += str(now_count + 1)
  result += ' '
print(result)
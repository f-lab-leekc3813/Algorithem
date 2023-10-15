n,k = map(int,input().split())

result = 0

coins = []

for _ in range(n):
  coin = int(input())
  coins.append(coin)

for i in reversed(range(n)):
  result += k // coins[i]
  k = k % coins[i]
print(result)
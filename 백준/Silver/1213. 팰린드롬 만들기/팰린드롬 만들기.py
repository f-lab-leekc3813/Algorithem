import collections
import sys

word = sys.stdin.readline().rstrip()
check_word = collections.Counter(word)
cnt = 0
result = ''
mid = ''

for k, v in list(check_word.items()):
  if v % 2 == 1 : # 홀수라면
    cnt += 1
    mid = k # 중간에 들어갈 값으로 저장
    if cnt >= 2: # 홀수인 값이 두개라면
      print("I'm Sorry Hansoo")
      exit()

for k, v in sorted(check_word.items()):
  result += (k * (v//2))
print(result + mid + result[::-1])
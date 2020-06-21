# dp[r+1:] : 감소 수열이기 때문에 자신보다 큰 값중에서 선택해야한다.
# [0] * 1002 : 1001로 하면 입력으로 1000이 들어왔을때 위의 식에서 1001 인덱스를 참조하기 때문에 에러 발생

n = int(input())
req = list(map(int, input().split()))
dp = [0] * 1002

for r in req:
    dp[r] = max(dp[r+1:]) + 1

print(max(dp))
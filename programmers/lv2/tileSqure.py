def solution(n):
    answer = 0
    dp = [0] * 600001

    dp[1], dp[2] = 1, 2
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007
    answer = dp[n] 
    return answer

print(solution(4))
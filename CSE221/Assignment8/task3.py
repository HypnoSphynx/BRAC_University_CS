import math
def coinC(coins, amount):
    dp = [math.inf] * (amount +1)
    dp[0] = 0  

    for i in coins:
        for j in range(i, amount + 1):
            dp[j] = min(dp[j], dp[j - i] + 1)
            
    if dp[amount]!=math.inf:
        return dp[amount]
    else:
        return -1

file=open('input3.txt')
output=open('output3.txt','w')
n,a= map(int,file.readline().split(' '))
coins=list(map(int,file.readline().split(' ')))
output.write(str(coinC(coins,a)))
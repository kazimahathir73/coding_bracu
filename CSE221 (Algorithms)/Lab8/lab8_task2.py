i = open("D:\CSE221\lab8_input2.txt",'r')
o = open("D:\CSE221\lab8_output2.txt",'w')

stairs = int(i.readline())
def climbStairs(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
o.write(str(climbStairs(stairs)))
def solve():
	n = int(input())
	s = input()
	x = [int(i) for i in input().split()]
	y = [int(i) for i in input().split()]

	"""
	dp[i][0]: the maximum happiness after day i if it's sunny
	dp[i][1]: the maximum happiness after day i if it's rainy
	
	if day i is sunny originally, then:
		dp[i][0]=max(
						dp[i-1][0] # sunny yesterday
						dp[i-1][1]+y[i-1] # rainy yesterday + sunny today, so we can get y[i-1] happiness
					)
		dp[i][1]=max(dp[i-1][0],dp[i-1][1])-x[i]
	
	if day i is rainy originally, then:
		dp[i][0]=max(
						dp[i-1][0]-x[i] # sunny yesterday
						dp[i-1][1]-x[i]+y[i-1] # rainy yesterday + sunny today, so we can get y[i-1] happiness
					)
		dp[i][1]=max(dp[i-1][0],dp[i-1][1])
		
	if day 1 is sunny, then:
		dp[1][0]=0
		dp[1][1]=-x[0]
	if day 1 is rainy, then:
		dp[1][0]=-x[0]
		dp[1][1]=0
	"""

	dp = [[float("-inf")] * 2 for _ in range(n)]
	if s[0] == 'S':
		dp[0][0] = 0
		dp[0][1] = -x[0]
	else:
		dp[0][0] = -x[0]
		dp[0][1] = 0
	for i in range(1, n):
		if s[i] == 'S':
			dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + y[i - 1])
			dp[i][1] = max(dp[i - 1][0], dp[i - 1][1]) - x[i]
		else:
			dp[i][0] = max(dp[i - 1][0] - x[i], dp[i - 1][1] - x[i] + y[i - 1])
			dp[i][1] = max(dp[i - 1][0], dp[i - 1][1])

	print(max(dp[-1]))


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

def solve():
	n = int(input())
	s = input()
	x = [int(i) for i in input().split()]
	y = [int(i) for i in input().split()]

	dp = [[float("-inf")] * 2 for _ in range(n)]
	if s[0] == 'S':
		dp[0][0] = 0
		dp[0][1] = -x[0]
	else:
		dp[0][0] = -x[0]
		dp[0][1] = 0

	for i in range(1, n):
		if s[i] == 'S':
			dp[i][0] = max(
				dp[i - 1][0],  # SS
				dp[i - 1][1] + y[i - 1]  # RS
			)
			dp[i][1] = max(dp[i - 1]) - x[i]
		else:
			dp[i][0] = max(
				dp[i - 1][0] - x[i],  # SS
				dp[i - 1][1] - x[i] + y[i - 1]  # RS
			)
			dp[i][1] = max(dp[i - 1])

	print(max(dp[-1]))


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

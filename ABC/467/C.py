def main():
	n, m = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	# dp[i][0]: the minimum cost to satisfy all((a[j]+a[j+1])%2==b[j]) for j in range(i) if a[i]==0
	# dp[i][1]: the minimum cost to satisfy all((a[j]+a[j+1])%2==b[j]) for j in range(i) if a[i]==1
	dp = [[float("inf")] * 2 for _ in range(n)]
	dp[0][0] = 0 if a[0] == 0 else 1
	dp[0][1] = 0 if a[0] == 1 else 1

	for i in range(1, n):
		match b[i - 1]:
			case 0:
				dp[i][0] = dp[i - 1][0] if a[i] == 0 else dp[i - 1][0] + 1
				dp[i][1] = dp[i - 1][1] if a[i] == 1 else dp[i - 1][1] + 1
			case 1:
				dp[i][0] = dp[i - 1][1] if a[i] == 0 else dp[i - 1][1] + 1
				dp[i][1] = dp[i - 1][0] if a[i] == 1 else dp[i - 1][0] + 1

	print(min(dp[-1]))


if __name__ == "__main__":
	main()

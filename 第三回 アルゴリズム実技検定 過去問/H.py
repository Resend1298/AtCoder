def main():
	n, l = [int(i) for i in input().split()]
	x = set(int(i) for i in input().split())
	t1, t2, t3 = [int(i) for i in input().split()]

	dp = [float("inf")] * (l + 1)
	dp[0] = 0
	dp[1] = t1 if 1 not in x else t1 + t3
	dp[2] = min(dp[1] + t1 if 2 not in x else dp[1] + t1 + t3, dp[0] + t1 + t2 if 2 not in x else dp[0] + t1 + t2 + t3)
	if l >= 3:
		dp[3] = min(dp[2] + t1 if 3 not in x else dp[2] + t1 + t3,
		            dp[1] + t1 + t2 if 3 not in x else dp[1] + t1 + t2 + t3)

	for i in range(4, l + 1):
		dp[i] = min(
			dp[i - 1] + t1 if i not in x else dp[i - 1] + t1 + t3,
			dp[i - 2] + t1 + t2 if i not in x else dp[i - 2] + t1 + t2 + t3,
			dp[i - 4] + t1 + t2 * 3 if i not in x else dp[i - 4] + t1 + t2 * 3 + t3
		)

	dp[l] = int(min(
		dp[l],
		dp[l - 1] + t1 // 2 + t2 // 2,
		dp[l - 2] + t1 // 2 + t2 * 1.5,
		dp[l - 3] + t1 // 2 + t2 * 2.5 if l >= 3 else float("inf")
	))

	print(dp[l])


if __name__ == "__main__":
	main()

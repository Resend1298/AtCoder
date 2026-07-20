def main():
	n, w_limit = [int(i) for i in input().split()]
	w, v = zip(*[[int(i) for i in input().split()] for _ in range(n)])

	dp = [[0] * (w_limit + 1) for _ in range(n)]
	for i in range(n):
		for j in range(w_limit + 1):
			dp[i][j] = max(dp[i - 1][j] if i - 1 >= 0 else 0,
			               dp[i - 1][j - w[i]] + v[i] if i - 1 >= 0 and j - w[i] >= 0 else 0,
			               v[i] if i == 0 and j - w[i] >= 0 else 0)

	print(max(dp[n - 1]))


if __name__ == "__main__":
	main()

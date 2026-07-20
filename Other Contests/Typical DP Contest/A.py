def main():
	n = int(input())
	p = [int(i) for i in input().split()]

	dp = [[False] * (sum(p) + 1) for _ in range(n)]
	for i in range(n):
		for j in range(sum(p) + 1):
			if ((i - 1 >= 0 and dp[i - 1][j])
					or (i == 0 and j == 0)
					or (i - 1 >= 0 and j - p[i] >= 0 and dp[i - 1][j - p[i]])
					or (i == 0 and j == p[i])):
				dp[i][j] = True

	print(dp[-1].count(True))


if __name__ == "__main__":
	main()

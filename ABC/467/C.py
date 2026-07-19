# TODO: review

def main():
	n, m = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	dp = [[0] * 2 for _ in range(n)]
	dp[0][1 - a[0]] = 1
	for i in range(1, n):
		match b[i - 1], a[i]:
			case 0, 0:
				dp[i][0] = dp[i - 1][0]
				dp[i][1] = 1 + dp[i - 1][1]
			case 0, 1:
				dp[i][0] = 1 + dp[i - 1][0]
				dp[i][1] = dp[i - 1][1]
			case 1, 0:
				dp[i][0] = dp[i - 1][1]
				dp[i][1] = 1 + dp[i - 1][0]
			case 1, 1:
				dp[i][0] = 1 + dp[i - 1][1]
				dp[i][1] = dp[i - 1][0]

	print(min(dp[-1]))


if __name__ == "__main__":
	main()

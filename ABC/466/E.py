# TODO: review

def main():
	n, k = [int(i) for i in input().split()]
	ab = [[int(i) for i in input().split()] for _ in range(n)]

	if n == 1:
		print(max(ab[0]))
		exit()
	if n == 2:
		if k == 1:
			print(max(
				ab[0][0] + ab[1][0],
				ab[0][1] + ab[1][0],
				ab[0][0] + ab[1][1]
			))
		else:
			print(max(
				ab[0][0] + ab[1][0],
				ab[0][1] + ab[1][0],
				ab[0][0] + ab[1][1],
				ab[0][1] + ab[1][1]
			))
		exit()

	for _ in range(k):
		dp = [[0] * 3 for _ in range(n)]
		dp[0][2] = ab[0][1] - ab[0][0]
		dp[1][1] = dp[0][2]
		dp[1][2] = max(0, dp[0][2]) + ab[1][1] - ab[1][0]

		for i in range(2, n):
			dp[i][1] = max(dp[i - 1][1], dp[i - 1][2])
			dp[i][2] = max(0, dp[i - 1][2]) + ab[i][1] - ab[i][0]

		if max(dp[-1]) == 0:
			break

		if dp[-1][2] >= dp[-1][1]:
			ab[-1][0], ab[-1][1] = ab[-1][1], ab[-1][0]
			for i in range(n - 2, -1, -1):
				if dp[i][2] > 0:
					ab[i][0], ab[i][1] = ab[i][1], ab[i][0]
				else:
					break
		else:
			for i in range(n - 2, -1, -1):
				if dp[i][1] >= dp[i][2]:
					continue
				for j in range(i, -1, -1):
					if dp[j][2] > 0:
						ab[j][0], ab[j][1] = ab[j][1], ab[j][0]
					else:
						break
				break

	print(sum(i[0] for i in ab))


if __name__ == "__main__":
	main()

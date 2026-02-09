# CPython TLE, PyPy AC

def main():
	n = int(input())
	grid = [input() for _ in range(n)]

	current_row_cost = [[0] * (n + 1) for _ in range(n)]
	for i in range(n):
		current_row_cost[i][0] = grid[i].count('.')
	for i in range(n):
		for j in range(1, n + 1):
			if grid[i][j - 1] == '.':
				current_row_cost[i][j] = current_row_cost[i][j - 1] - 1
			else:
				current_row_cost[i][j] = current_row_cost[i][j - 1] + 1

	dp = [[0] * (n + 1) for _ in range(n)]
	pre_row_min_dp = [0] * (n + 1)
	for i in range(n):
		for j in range(n + 1):
			dp[i][j] = current_row_cost[i][j] + pre_row_min_dp[j]
		pre_row_min_dp[-1] = dp[i][-1]
		for j in range(n - 1, -1, -1):
			pre_row_min_dp[j] = min(pre_row_min_dp[j + 1], dp[i][j])

	print(min(dp[-1]))


if __name__ == "__main__":
	main()

def main():
	n, k = [int(i) for i in input().split()]
	a, b = [list(i) for i in zip(*[[int(i) for i in input().split()] for _ in range(n)])]

	for _ in range(k):
		dp: list[list[int | float]] = [[0] * 2 for _ in range(n)]
		"""
		For any card, we can either choose to flip it or not.
		Note that there's actually 2 states for not flipping the card:
			- Not flipping it, and haven't flipped any card previously (still possible to flip cards later)
			- Not flipping it, but have flipped cards previously (not possible to flip cards later)
		Luckily, for the first state, the gain is always 0, so we don't need to calculate or store it.

		Therefore, the dp state is defined as follows:
			- dp[i][0]: The maximum gain we can get by considering cards up to i, not flipping the i-th card, and have flipped cards previously.
			- dp[i][1]: The maximum gain we can get by considering cards up to i, flipping the i-th card.

		We can then derive the following recurrence relations:
			- dp[i][0] = max(dp[i-1][0],  # flip range was already over before card i-1
			                 dp[i-1][1])  # flip cards [..., i-1]

			- dp[i][1] = max(0,           # flip range starts at card i
			                 dp[i-1][1]   # flip range continues from card i-1
			                 ) + b[i] - a[i]  # gain from flipping card i

		Finally there's a special case:
			max(0, dp[-1][0], dp[-1][1]) == 0 means that we should not flip any card, and we can stop here.
		"""

		dp[0][0] = float("-inf")  # not legal
		dp[0][1] = b[0] - a[0]
		for i in range(1, n):
			dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
			dp[i][1] = max(0, dp[i - 1][1]) + b[i] - a[i]

		if max(0, dp[-1][0], dp[-1][1]) == 0:
			break

		# flip cards based on the dp table
		l, r = -1, -1
		for i in range(n - 1, -1, -1):
			if dp[i][1] > dp[i][0] and dp[i][1] > 0:
				r = i
				break
		for i in range(r, -1, -1):
			if i - 1 == -1 or dp[i - 1][1] <= 0:
				l = i
				break
		for i in range(l, r + 1):
			a[i], b[i] = b[i], a[i]

	print(sum(a))


if __name__ == "__main__":
	main()

def main():
	n = int(input())
	t = input()

	"""
	S is beautiful -> s[0] XNOR s[1] XNOR ... XNOR s[-1] == 1 -> s.count('0') is even
	
	- calculation order does not matter in XNOR, therefore S is beautiful -> s[0] XNOR s[1] XNOR ... XNOR s[-1] == 1
	- for any S, since the order does not matter for XNOR, its result is the same as 0...01...1's result
		1 XNOR 1 XNOR ... XNOR 1 == 1 -> 0...01
		if 0's count is even, all 0s cancel out -> 1 XNOR 1 == 1 -> beautiful
		if 0's count is odd, all 0s cancel out except one -> 0 XNOR 1 == 0 -> not beautiful
		therefore, S is beautiful == s.count('0') is even
	"""

	# dp[i][0]: count of substrings with even count of '0's ending at index i
	# dp[i][1]: count of substrings with odd count of '0's ending at index i
	# therefore, result is sum(dp[i][0])
	dp = [[0] * 2 for _ in range(n)]
	dp[0][0] = 1 if t[0] == '1' else 0
	dp[0][1] = 1 if t[0] == '0' else 0
	for i in range(1, n):
		if t[i] == '0':
			dp[i][0] = dp[i - 1][1]
			dp[i][1] = dp[i - 1][0] + 1
		else:
			dp[i][0] = dp[i - 1][0] + 1
			dp[i][1] = dp[i - 1][1]

	print(sum(i[0] for i in dp))


if __name__ == "__main__":
	main()

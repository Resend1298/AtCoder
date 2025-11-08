def main():
	n = int(input())
	head_weight = 0
	body_weight = 0
	parts = []
	result = 0
	for _ in range(n):
		w, h, b = [int(i) for i in input().split()]
		if b >= h:
			body_weight += w
			result += b
		else:
			parts.append((w, h, b))
			body_weight += w
			result += b

	n = len(parts)
	w = body_weight
	weight = [i[0] * 2 for i in parts]
	value = [i[1] - i[2] for i in parts]
	dp = [0] * (w + 1)
	for i in range(n):
		for l in range(w, weight[i] - 1, -1):
			dp[l] = max(dp[l], dp[l - weight[i]] + value[i])

	result += dp[w]
	print(result)


if __name__ == "__main__":
	main()

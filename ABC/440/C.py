def solve():
	n, w = [int(i) for i in input().split()]
	c = [int(i) for i in input().split()]

	cost_sum = [0] * (w * 2)
	for i in range(n):
		cost_sum[(i + 1) % (w * 2)] += c[i]

	result = sum(cost_sum[:w])
	current = result

	for i in range(w, w * 2):
		current = current + cost_sum[i] - cost_sum[i - w]
		result = min(result, current)
	for i in range(w - 1):
		current = current + cost_sum[i] - cost_sum[i + w]
		result = min(result, current)

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

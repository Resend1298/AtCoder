def solve():
	n, w = [int(i) for i in input().split()]
	c = [int(i) for i in input().split()]

	cost_sum = [0] * (w * 2)
	for i in range(n):
		cost_sum[(i + 1) % (w * 2)] += c[i]

	cost_sum += cost_sum[:w - 1]
	result = current = sum(cost_sum[:w])
	for i in range(w * 2 - 1):
		current = current - cost_sum[i] + cost_sum[i + w]
		result = min(result, current)

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

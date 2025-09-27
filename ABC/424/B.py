def main():
	n, m, k = [int(i) for i in input().split()]

	ac_count = [0] * n
	result = []

	for _ in range(k):
		a, _ = [int(i) - 1 for i in input().split()]
		ac_count[a] += 1
		if ac_count[a] == m:
			result.append(a + 1)

	print(*result)


if __name__ == "__main__":
	main()

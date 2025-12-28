def main():
	n, m = [int(i) for i in input().split()]
	s = [int(i) for i in list(input())]
	t = [int(i) for i in list(input())]

	result = float("inf")

	for i in range(n - m + 1):
		result = min(result, sum((s[i + j] - t[j]) % 10 for j in range(m)))

	print(result)


if __name__ == "__main__":
	main()

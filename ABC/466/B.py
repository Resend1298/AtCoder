def main():
	n, m = [int(i) for i in input().split()]
	cs = [[int(i) for i in input().split()] for _ in range(n)]

	result = [-1] * m
	for c, s in cs:
		result[c - 1] = max(result[c - 1], s)

	print(*result)


if __name__ == "__main__":
	main()

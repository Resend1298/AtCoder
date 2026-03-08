def main():
	n, m = [int(i) for i in input().split()]
	c = [int(i) for i in input().split()]
	ab = [[int(i) for i in input().split()] for _ in range(n)]

	result = 0

	for a, b in ab:
		limit = min(b, c[a - 1])
		result += limit
		c[a - 1] -= limit

	print(result)


if __name__ == "__main__":
	main()

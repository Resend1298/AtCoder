def main():
	n = int(input())

	result: list[list[int | None]] = [[None] * n for _ in range(n)]

	r = 0
	c = (n - 1) // 2
	k = 1
	result[r][c] = k

	for _ in range(n ** 2 - 1):
		if result[(r - 1) % n][(c + 1) % n] is None:
			r = (r - 1) % n
			c = (c + 1) % n
		else:
			r = (r + 1) % n
		k += 1
		result[r][c] = k

	for i in result:
		print(*i)


if __name__ == "__main__":
	main()

def main():
	n, m = [int(i) for i in input().split()]

	result = [0] * n
	current = 0

	for _ in range(m):
		result[current] += 1
		current += 1
		if current == n:
			current = 0

	for i in result:
		print(i)


if __name__ == "__main__":
	main()

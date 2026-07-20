def main():
	n, m = [int(i) for i in input().split()]
	ab = [[int(i) - 1 for i in input().split()] for _ in range(n)]

	result = [0] * m
	for a, b in ab:
		result[a] -= 1
		result[b] += 1

	for i in result:
		print(i)


if __name__ == "__main__":
	main()

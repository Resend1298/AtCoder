def main():
	n, m = [int(i) for i in input().split()]
	ab = []
	for _ in range(m):
		a, b = [int(i) for i in input().split()]
		ab.append((a - b, a))

	ab.sort()
	result = 0

	for i, j in ab:
		if n >= j:
			count = (n - j) // i + 1
			n -= i * count
			result += count

	print(result)


if __name__ == "__main__":
	main()

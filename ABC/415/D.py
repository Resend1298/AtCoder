def main():
	n, m = [int(i) for i in input().split()]
	diff = []
	min_a = float("inf")
	for i in range(m):
		ab = [int(i) for i in input().split()]
		diff.append((ab[0] - ab[1], ab[0]))
		min_a = min(min_a, ab[0])

	diff.sort()

	result = 0

	for i, j in diff:
		if n >= j:
			count = (n - j) // i + 1
			result += count
			n -= count * i
		# while n >= j:
		# 	n -= i
		# 	result += 1
		if n < min_a:
			break

	print(result)


if __name__ == "__main__":
	main()

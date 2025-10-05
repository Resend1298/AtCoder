def main():
	n, q = [int(i) for i in input().split()]

	min_version = 1
	version_count = [1] * (n + 1)

	for _ in range(q):
		x, y = [int(i) for i in input().split()]

		if x < min_version:
			print(0)
			continue

		result = sum(version_count[min_version:x + 1])
		print(result)
		version_count[y] += result
		min_version = x + 1


if __name__ == "__main__":
	main()

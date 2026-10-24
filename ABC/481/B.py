def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	result = 0

	for i in range(n - 1):
		if a[i] < k < a[i + 1] or a[i] > k > a[i + 1]:
			result += 1

	for i in a:
		if i == k:
			result += 1

	print(result)


if __name__ == "__main__":
	main()

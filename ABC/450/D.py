def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	a = [i % k for i in a]
	a.sort()
	result = a[-1] - a[0]

	for i in range(n - 1):
		result = min(result, a[i] + k - a[i + 1])

	print(result)


if __name__ == "__main__":
	main()

def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	result = 0
	for i in range(n - 2):
		if a[i] < a[i + 1] > a[i + 2]:
			result += 1

	print(result)


if __name__ == "__main__":
	main()

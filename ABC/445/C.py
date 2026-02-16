def main():
	n = int(input())
	a = [int(i) - 1 for i in input().split()]

	for i in range(n - 1, -1, -1):
		a[i] = a[a[i]]

	print(*[i + 1 for i in a])


if __name__ == "__main__":
	main()

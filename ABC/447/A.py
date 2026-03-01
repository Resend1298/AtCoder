def main():
	n, m = [int(i) for i in input().split()]

	available = n // 2 if n % 2 == 0 else n // 2 + 1

	if available >= m:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

def main():
	n, m = [int(i) for i in input().split()]

	if m <= (n + 1) // 2:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

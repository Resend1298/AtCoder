def main():
	a, b, c, d = [int(i) for i in input().split()]

	if c >= a and d < b:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

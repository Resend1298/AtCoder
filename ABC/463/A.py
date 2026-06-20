def main():
	x, y = [int(i) for i in input().split()]

	if x * 9 == y * 16:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

def main():
	a, b, c = [int(i) for i in input().split()]

	if a != b and b == c:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

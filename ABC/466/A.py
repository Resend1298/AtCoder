def main():
	_ = int(input())
	x = [int(i) for i in input().split()]

	if all(i < 0 for i in x):
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

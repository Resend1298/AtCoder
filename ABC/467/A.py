def main():
	h, w = [int(i) for i in input().split()]

	if 10000 * w >= 25 * h ** 2:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

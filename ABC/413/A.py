def main():
	n, m = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	if sum(a) <= m:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

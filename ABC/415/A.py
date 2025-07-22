def main():
	_ = int(input())
	a = [int(i) for i in input().split()]
	x = int(input())

	print("Yes" if x in a else "No")


if __name__ == "__main__":
	main()

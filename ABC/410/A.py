def main():
	_ = int(input())
	a = [int(i) for i in input().split()]
	k = int(input())

	print([k <= i for i in a].count(True))


if __name__ == "__main__":
	main()

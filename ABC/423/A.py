def main():
	x, c = [int(i) for i in input().split()]
	print(x // (1000 + c) * 1000)


if __name__ == "__main__":
	main()

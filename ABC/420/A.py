def main():
	x, y = [int(i) for i in input().split()]

	result = (x + y) % 12
	print(result if result != 0 else 12)


if __name__ == "__main__":
	main()

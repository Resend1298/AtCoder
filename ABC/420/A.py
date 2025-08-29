def main():
	x, y = [int(i) for i in input().split()]

	result = (x + y) % 12
	if result == 0:
		result = 12

	print(result)


if __name__ == "__main__":
	main()

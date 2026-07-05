def main():
	x, y, l, r, a, b = [int(i) for i in input().split()]

	result = 0
	for i in range(a, b):
		if l <= i < r:
			result += x
		else:
			result += y

	print(result)


if __name__ == "__main__":
	main()

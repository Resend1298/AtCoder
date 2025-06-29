def main():
	n = int(input())

	result = 0

	for _ in range(n):
		a, b = [int(i) for i in input().split()]
		if b > a:
			result += 1

	print(result)


if __name__ == "__main__":
	main()

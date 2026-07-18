def main():
	n = int(input())

	result = 0

	for _ in range(n):
		a, b, s = input().split()
		if s == "keep":
			result += int(b) - int(a)

	print(result)


if __name__ == "__main__":
	main()

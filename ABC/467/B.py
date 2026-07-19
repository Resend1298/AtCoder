def main():
	n = int(input())
	abs_ = [input().split() for _ in range(n)]

	result = 0

	for a, b, s in abs_:
		if s == "keep":
			result += int(b) - int(a)

	print(result)


if __name__ == "__main__":
	main()

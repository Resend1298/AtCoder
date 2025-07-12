def main():
	n = int(input())

	if n % 2 == 0:
		max_c = n // 2 - 1
	else:
		max_c = n // 2

	result = 0
	for c in range(1, max_c + 1):
		for b in range(c + 1, n - c + 1):
			for i in range(1, (n - c) // b + 1):
				a = i * b + c
				if a != b and a != c:
					result += 1

	print(result % 998244353)


if __name__ == "__main__":
	main()

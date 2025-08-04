def main():
	_ = int(input())
	s = input()

	count = [0] * 26
	for i in s:
		count[ord(i) - ord('a')] += 1

	result = 1
	for i in count:
		result *= i + 1
	result -= 1

	print(result % (10 ** 9 + 7))


if __name__ == "__main__":
	main()

def main():
	s = input()

	l = 0
	r = 0
	result = 0

	while l < len(s):
		while r + 1 < len(s) and s[r] != s[r + 1]:
			r += 1

		result += (r - l + 2) * (r - l + 1) // 2
		result %= 998244353

		l = r + 1
		r = l

	print(result)


if __name__ == "__main__":
	main()

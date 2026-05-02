def main():
	s = input()

	l = 0
	r = 0
	result = 0

	while l < len(s):
		while r + 1 < len(s) and s[r + 1] != s[r]:
			r += 1

		result = (result + (r - l + 1) * (r - l + 2) // 2) % 998244353

		l = r + 1
		r = l

	print(result)


if __name__ == "__main__":
	main()

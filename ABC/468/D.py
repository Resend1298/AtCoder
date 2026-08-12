# CPython TLE, PyPy AC

def main():
	s = input()

	result = 0

	# substrings which length is odd
	for center in range(len(s)):
		result += 1
		diff_count = 0

		# noinspection DuplicatedCode
		for l, r in zip(range(center - 1, -1, -1), range(center + 1, len(s))):
			if s[l] != s[r]:
				diff_count += 1
			if diff_count > 1:
				break
			result += 1

	# substrings which length is even
	for l in range(len(s) - 1):
		r = l + 1
		result += 1
		diff_count = 0 if s[l] == s[r] else 1

		# noinspection DuplicatedCode,assignment-to-loop-or-with-parameter
		for l, r in zip(range(l - 1, -1, -1), range(r + 1, len(s))):
			if s[l] != s[r]:
				diff_count += 1
			if diff_count > 1:
				break
			result += 1

	print(result)


if __name__ == "__main__":
	main()

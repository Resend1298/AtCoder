def main():
	s = input()

	rle_s = []
	pre_char = s[0]
	pre_count = 1
	for i in range(1, len(s)):
		if s[i] == pre_char:
			pre_count += 1
		else:
			rle_s.append((pre_char, pre_count))
			pre_char = s[i]
			pre_count = 1
	rle_s.append((pre_char, pre_count))

	result = 0

	for i in range(len(rle_s) - 1):
		if int(rle_s[i][0]) + 1 != int(rle_s[i + 1][0]):
			continue

		result += min(rle_s[i][1], rle_s[i + 1][1])

	print(result)


if __name__ == "__main__":
	main()

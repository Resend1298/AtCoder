# TODO: review

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

	current = {'a': 0, 'b': 0, 'c': 0}
	for char, count in rle_s:
		new = {'a': 0, 'b': 0, 'c': 0}

		for k, v in current.items():
			if k != char:
				new[char] += v * count

		new[char] += count

		for k, v in current.items():
			new[k] += v

		for i in new:
			new[i] = new[i] % 998244353

		current = new

	print(sum(current.values()) % 998244353)


if __name__ == "__main__":
	main()

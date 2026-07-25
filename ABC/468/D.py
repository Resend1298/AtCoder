def main():
	s = input()

	len_s = len(s)
	result = len_s

	for center in range(len_s):
		max_len = min(center, len_s - center - 1)
		chance = True
		for i in range(1, max_len + 1):
			if s[center - i] != s[center + i]:
				if chance:
					chance = False
				else:
					break
			result += 1

		if center != len_s - 1:
			max_len = min(center + 1, len_s - center - 1)
			chance = True
			for i in range(1, max_len + 1):
				if s[center - i + 1] != s[center + i]:
					if chance:
						chance = False
					else:
						break
				result += 1

	print(result)


if __name__ == "__main__":
	main()

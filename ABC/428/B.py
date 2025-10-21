from collections import Counter


def main():
	n, k = [int(i) for i in input().split()]
	s = input()

	substr_counter = Counter(s[i:i + k] for i in range(n - k + 1))

	max_count = substr_counter.most_common(1)[0][1]
	# noinspection SpellCheckingInspection
	max_count_substrs = [i[0] for i in substr_counter.most_common() if i[1] == max_count]
	max_count_substrs.sort()

	print(max_count)
	print(*max_count_substrs)


if __name__ == "__main__":
	main()

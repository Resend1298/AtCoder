from sortedcontainers import SortedList


def main():
	n, l, r = [int(i) for i in input().split()]
	s = input()

	alphabet_index = [SortedList() for _ in range(26)]
	for i, c in enumerate(s):
		alphabet_index[ord(c) - ord('a')].add(i)

	result = 0
	for i in alphabet_index:
		for j in i:
			result += i.bisect_right(j + r) - i.bisect_left(j + l)

	print(result)


if __name__ == "__main__":
	main()

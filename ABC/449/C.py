from sortedcontainers import SortedList


def main():
	n, l, r = [int(i) for i in input().split()]
	s = input()

	index_sl = [SortedList() for _ in range(26)]
	for i, c in enumerate(s):
		index_sl[ord(c) - ord('a')].add(i)

	result = 0
	for i in index_sl:
		for j in i:
			left = i.bisect_left(j + l)
			if left == len(i):
				break
			right = i.bisect_right(j + r) - 1
			if right == -1:
				break
			if left <= right:
				result += right - left + 1

	print(result)


if __name__ == "__main__":
	main()

from sortedcontainers import SortedList


def main():
	_, _ = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	a.sort()
	b = SortedList(b)
	result = 0

	for i in a:
		index = b.bisect_right(2 * i) - 1
		if index != -1:
			b.pop(index)
			result += 1

	print(result)


if __name__ == "__main__":
	main()

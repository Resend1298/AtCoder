# TODO: review

from sortedcontainers import SortedList


def main():
	n, m = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	b.sort()
	b_prefixsum = [0]
	for i in b:
		b_prefixsum.append(b_prefixsum[-1] + i)
	b = SortedList(b)

	result = 0
	for i in a:
		smaller_equal_index = b.bisect_right(i) - 1
		if smaller_equal_index != -1:
			result += i * (smaller_equal_index + 1) - b_prefixsum[smaller_equal_index + 1]
		if smaller_equal_index != m - 1:
			result += b_prefixsum[m] - b_prefixsum[smaller_equal_index + 1] - i * (m - (smaller_equal_index + 1))
		result %= 998244353

	print(result)


if __name__ == "__main__":
	main()

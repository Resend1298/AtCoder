from sortedcontainers import SortedList


def main():
	n, m = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	b = SortedList(b)
	b_prefix_sum = [0]
	for i in b:
		b_prefix_sum.append(b_prefix_sum[-1] + i)
	result = 0

	for i in a:
		less_than_or_equal_index = b.bisect_right(i) - 1
		if less_than_or_equal_index != -1:
			result += i * (less_than_or_equal_index + 1) - b_prefix_sum[less_than_or_equal_index + 1]
		if less_than_or_equal_index != m - 1:
			result += b_prefix_sum[m] - b_prefix_sum[less_than_or_equal_index + 1] - i * (
					m - less_than_or_equal_index - 1)
		result %= 998244353

	print(result)


if __name__ == "__main__":
	main()

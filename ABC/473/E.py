from bisect import bisect_left
from collections import defaultdict


def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	prefix_sum = [0]
	for i in a:
		prefix_sum.append((prefix_sum[-1] + i) % k)

	prefix_sum_sl = defaultdict(list)
	for i, j in enumerate(prefix_sum):
		prefix_sum_sl[j].append(i)

	result = 0
	target_index = float("-inf")

	for i in range(n, -1, -1):
		if i == target_index:
			result += 1
			target_index = float("-inf")

		possible_index = bisect_left(prefix_sum_sl[prefix_sum[i]], i) - 1
		if possible_index == -1:
			continue
		possible_index = prefix_sum_sl[prefix_sum[i]][possible_index]

		if possible_index > target_index:
			target_index = possible_index

	print(result)


if __name__ == "__main__":
	main()

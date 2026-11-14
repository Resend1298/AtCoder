from bisect import bisect_left
from collections import defaultdict


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	rle_a = []
	pre_char = a[0]
	pre_index = 0
	pre_count = 1
	for i in range(1, len(a)):
		if a[i] == pre_char:
			pre_count += 1
			continue
		else:
			rle_a.append((pre_char, pre_index, pre_count))
			pre_char = a[i]
			pre_index = i
			pre_count = 1
	rle_a.append((pre_char, pre_index, pre_count))

	num_to_index = defaultdict(list)
	for i, j, k in rle_a:
		num_to_index[i].append((j, k))
	num_to_index_prefix_sum = defaultdict(list)
	for i in num_to_index:
		num_to_index_prefix_sum[i] = [0]
		for j, k in num_to_index[i]:
			num_to_index_prefix_sum[i].append(num_to_index_prefix_sum[i][-1] + k)

	result = 1

	for i in range(1, len(rle_a)):
		j, k, _ = rle_a[i]
		bisect_index = bisect_left(num_to_index[j], (k, 0)) - 1
		result += k - num_to_index_prefix_sum[j][bisect_index + 1]

	print(result)


if __name__ == "__main__":
	main()

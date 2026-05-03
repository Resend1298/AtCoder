from collections import defaultdict

from sortedcontainers import SortedList


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	numbers_index = defaultdict(SortedList)
	for i in range(n):
		numbers_index[a[i]].add(i)
	result = 0

	for j in range(n):
		if a[j] % 5 != 0:
			continue

		ai = a[j] // 5 * 7
		ak = a[j] // 5 * 3

		# min(i, j, k) = j
		i_index = numbers_index[ai].bisect_right(j)
		k_index = numbers_index[ak].bisect_right(j)
		if i_index != len(numbers_index[ai]) and k_index != len(numbers_index[ak]):
			result += (len(numbers_index[ai]) - i_index) * (len(numbers_index[ak]) - k_index)

		# max(i, j, k) = j
		i_index = numbers_index[ai].bisect_left(j) - 1
		k_index = numbers_index[ak].bisect_left(j) - 1
		if i_index != -1 and k_index != -1:
			result += (i_index + 1) * (k_index + 1)

	print(result)


if __name__ == "__main__":
	main()

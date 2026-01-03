from collections import defaultdict

from sortedcontainers import SortedList


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	a_sortedlist = defaultdict(SortedList)
	for i in range(n):
		a_sortedlist[a[i]].add(i)
	result = 0

	for i in range(n):
		if a[i] % 5 != 0:
			continue

		target_i = a[i] // 5 * 7
		target_k = a[i] // 5 * 3

		if target_i not in a_sortedlist or target_k not in a_sortedlist:
			continue

		search_i_left = a_sortedlist[target_i].bisect_right(i)
		search_i_right = a_sortedlist[target_i].bisect_left(n) - 1
		search_k_left = a_sortedlist[target_k].bisect_right(i)
		search_k_right = a_sortedlist[target_k].bisect_left(n) - 1
		if (search_i_left != n and search_i_right != -1 and search_i_left <= search_i_right and
				search_k_left != n and search_k_right != -1 and search_k_left <= search_k_right):
			result += (search_i_right - search_i_left + 1) * (search_k_right - search_k_left + 1)

		search_i_left = a_sortedlist[target_i].bisect_right(-1)
		search_i_right = a_sortedlist[target_i].bisect_left(i) - 1
		search_k_left = a_sortedlist[target_k].bisect_right(-1)
		search_k_right = a_sortedlist[target_k].bisect_left(i) - 1
		if (search_i_left != n and search_i_right != -1 and search_i_left <= search_i_right and
				search_k_left != n and search_k_right != -1 and search_k_left <= search_k_right):
			result += (search_i_right - search_i_left + 1) * (search_k_right - search_k_left + 1)

	print(result)


if __name__ == "__main__":
	main()

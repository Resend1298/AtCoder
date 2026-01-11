# TODO: review

from sortedcontainers import SortedList


def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	a.sort()
	a_sortedlist = SortedList(a)
	a_diff = [a[i + 1] - a[i] - 1 for i in range(n - 1)]
	prefix_sum = [0]
	for i in a_diff:
		prefix_sum.append(prefix_sum[-1] + i)
	prefix_sum_sortedlist = SortedList(prefix_sum)

	for _ in range(q):
		x, y = [int(i) for i in input().split()]

		next_a = a_sortedlist.bisect_left(x)
		if next_a == n:
			print(x + y - 1)
			continue

		usable_from_x_to_next_a = a[next_a] - x
		if usable_from_x_to_next_a >= y:
			print(x + y - 1)
			continue
		y -= usable_from_x_to_next_a
		x_index = next_a

		if prefix_sum[-1] - prefix_sum[x_index] < y:
			print(a[-1] + (y - (prefix_sum[-1] - prefix_sum[x_index])))
			continue

		index = prefix_sum_sortedlist.bisect_left(y + prefix_sum[x_index])
		x = a[index - 1]
		y -= prefix_sum[index - 1] - prefix_sum[x_index]
		print(x + y)


if __name__ == "__main__":
	main()

from sortedcontainers import SortedList


def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	a.sort()
	a_sortedlist = SortedList(a)
	space = [a[i + 1] - a[i] - 1 for i in range(n - 1)]
	space_prefix_sum = [0]
	for i in space:
		space_prefix_sum.append(space_prefix_sum[-1] + i)
	space_prefix_sum_sortedlist = SortedList(space_prefix_sum)

	for _ in range(q):
		x, y = [int(i) for i in input().split()]

		right_a_index = a_sortedlist.bisect_left(x)
		if right_a_index == n:
			print(x + y - 1)
			continue

		spaces_until_right_a = a[right_a_index] - x
		if spaces_until_right_a >= y:
			print(x + y - 1)
			continue
		y -= spaces_until_right_a

		enough_space_index = space_prefix_sum_sortedlist.bisect_left(y + space_prefix_sum[right_a_index])
		if enough_space_index == n:
			print(y - space_prefix_sum[-1] + space_prefix_sum[right_a_index] + a[-1])
			continue
		y -= space_prefix_sum[enough_space_index - 1] - space_prefix_sum[right_a_index]

		print(a[enough_space_index - 1] + y)


if __name__ == "__main__":
	main()

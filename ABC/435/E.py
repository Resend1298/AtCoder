from sortedcontainers import SortedKeyList


def main():
	n, q = [int(i) for i in input().split()]

	black_count = 0
	black_range = SortedKeyList(key=lambda x: x[0])

	for _ in range(q):
		l, r = [int(i) - 1 for i in input().split()]

		left_index = black_range.bisect_key_right(l) - 1
		if left_index != -1 and black_range[left_index][1] >= l:
			left_l, left_r = black_range.pop(left_index)
			black_count -= left_r - left_l + 1
			l = left_l
			r = max(r, left_r)

		right_index = black_range.bisect_key_right(l)
		while right_index != len(black_range) and r >= black_range[right_index][0]:
			right_l, right_r = black_range.pop(right_index)
			black_count -= right_r - right_l + 1
			r = max(r, right_r)

		black_range.add((l, r))
		black_count += r - l + 1
		print(n - black_count)


if __name__ == "__main__":
	main()

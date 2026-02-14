from collections import defaultdict
from sys import setrecursionlimit

from sortedcontainers import SortedList


def solve(current_h, current_w, wide, tall, shape_to_index, result):
	widest_w, widest_h = wide.pop(0)
	tall.remove((widest_w, widest_h))
	index = shape_to_index[(widest_w, widest_h)].pop()
	result[index][0] = current_h - widest_h + 1
	result[index][1] = 1

	if widest_w == current_w:
		if current_h - widest_h > 0 and current_w > 0:
			solve(current_h - widest_h, current_w, wide, tall, shape_to_index, result)
	else:
		remain_wide = current_w - widest_w
		while remain_wide > 1:
			highest_w, highest_h = tall.pop(0)
			wide.remove((highest_w, highest_h))
			index = shape_to_index[(highest_w, highest_h)].pop()
			result[index][0] = 1
			result[index][1] = widest_w + remain_wide - highest_w + 1
			remain_wide -= highest_w
		if remain_wide == 1:
			remain_height = current_h
			while remain_height > 0:
				highest_w, highest_h = tall.pop(0)
				wide.remove((highest_w, highest_h))
				index = shape_to_index[(highest_w, highest_h)].pop()
				result[index][0] = remain_height - highest_h + 1
				result[index][1] = widest_w + 1
				remain_height -= highest_h
		if current_h - widest_h > 0 and widest_w > 0:
			solve(current_h - widest_h, widest_w, wide, tall, shape_to_index, result)


def main():
	h_, w_, n = [int(i) for i in input().split()]
	wide = SortedList(key=lambda x: (-x[0], -x[1]))
	tall = SortedList(key=lambda x: (-x[1], -x[0]))
	shape_to_index = defaultdict(list)
	for i in range(n):
		h, w = [int(i) for i in input().split()]
		shape_to_index[(w, h)].append(i)
		wide.add((w, h))
		tall.add((w, h))

	result = [[-1] * 2 for _ in range(n)]

	setrecursionlimit(10 ** 7)
	solve(h_, w_, wide, tall, shape_to_index, result)

	for x, y in result:
		print(x, y)


if __name__ == "__main__":
	main()

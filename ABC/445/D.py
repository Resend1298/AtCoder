from sys import setrecursionlimit

from sortedcontainers import SortedList


def recursion(wide_sl, height_sl, result, h, w):
	if not wide_sl:
		return

	widest_id, widest_w, widest_h = wide_sl[-1]
	tallest_id, tallest_w, tallest_h = height_sl[-1]

	if widest_w == w:
		wide_sl.pop()
		height_sl.remove((widest_id, widest_w, widest_h))
		result[widest_id][0] = h - widest_h + 1
		result[widest_id][1] = 1
		recursion(wide_sl, height_sl, result, h - widest_h, w)
	else:
		height_sl.pop()
		wide_sl.remove((tallest_id, tallest_w, tallest_h))
		result[tallest_id][0] = 1
		result[tallest_id][1] = w - tallest_w + 1
		recursion(wide_sl, height_sl, result, h, w - tallest_w)


def main():
	h, w, n = [int(i) for i in input().split()]
	pieces = []
	for i in range(n):
		h_, w_ = [int(i) for i in input().split()]
		pieces.append((i, w_, h_))

	wide_sl = SortedList(pieces, key=lambda x: (x[1], x[2], x[0]))
	height_sl = SortedList(pieces, key=lambda x: (x[2], x[1], x[0]))
	result = [[0] * 2 for _ in range(n)]

	setrecursionlimit(10 ** 7)
	recursion(wide_sl, height_sl, result, h, w)

	for i in result:
		print(*i)


if __name__ == "__main__":
	main()

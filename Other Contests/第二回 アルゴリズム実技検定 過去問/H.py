from collections import defaultdict


def main():
	n, m = [int(i) for i in input().split()]
	a = [input() for _ in range(n)]

	digit_index = [[] for _ in range(10)]
	for i in range(n):
		for j in range(m):
			match a[i][j]:
				case 'S':
					sx, sy = i, j
				case 'G':
					gx, gy = i, j
				case _:
					digit_index[int(a[i][j])].append((i, j))

	if any(not digit_index[i] for i in range(1, 10)):
		print(-1)
		exit()

	cost = defaultdict(lambda: float("inf"))
	for i in range(1, 10):
		if i == 1:
			for new_x, new_y in digit_index[1]:
				# noinspection PyUnboundLocalVariable
				cost[(new_x, new_y)] = abs(new_x - sx) + abs(new_y - sy)
		else:
			for new_x, new_y in digit_index[i]:
				for old_x, old_y in digit_index[i - 1]:
					cost[(new_x, new_y)] = min(cost[(new_x, new_y)],
					                           cost[(old_x, old_y)] + abs(new_x - old_x) + abs(new_y - old_y))

	# noinspection PyUnboundLocalVariable
	print(min(cost[(x, y)] + abs(x - gx) + abs(y - gy) for x, y in digit_index[9]))


if __name__ == "__main__":
	main()

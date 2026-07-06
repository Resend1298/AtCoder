# CPython TLE, PyPy AC

from collections import deque
from itertools import product

DIRECTION_MAP = ((-1, 0), (1, 0), (0, -1), (0, 1))  # up, down, left, right
DIRECTION_CHAR = "UDLR"


def main():
	h, w = [int(i) for i in input().split()]
	s = [input() for _ in range(h)]

	sx, sy = -1, -1
	for i, j in product(range(h), range(w)):
		if s[i][j] == 'S':
			sx, sy = i, j
			break

	q = deque()
	visited = [[[False] * 4 for _ in range(w)] for _ in range(h)]
	q.append((sx, sy, 0, 0))  # x, y, previous direction, cost
	visited[sx][sy] = [True] * 4
	pre = [[[-1] * 4 for _ in range(w)] for _ in range(h)]

	while q:
		x, y, prev_dir, cost = q.popleft()

		if s[x][y] == 'G':
			print("Yes")
			result = []
			while x != sx or y != sy:
				result.append(DIRECTION_CHAR[prev_dir])
				dx, dy = DIRECTION_MAP[prev_dir]
				x, y, prev_dir = x - dx, y - dy, pre[x][y][prev_dir]
			print(''.join(result[::-1]))
			exit()

		if cost >= 5000000:
			print("No")
			exit()

		for next_x, next_y, next_dir in [(x - 1, y, 0), (x + 1, y, 1), (x, y - 1, 2), (x, y + 1, 3)]:
			if 0 <= next_x < h and 0 <= next_y < w and not visited[next_x][next_y][next_dir] and s[next_x][
				next_y] != '#':
				if s[x][y] == 'o' and next_dir != prev_dir:
					continue
				if s[x][y] == 'x' and next_dir == prev_dir:
					continue

				if s[next_x][next_y] == '.':
					q.append((next_x, next_y, next_dir, cost + 1))
					visited[next_x][next_y] = [True] * 4
					pre[next_x][next_y] = [prev_dir] * 4
				else:
					q.append((next_x, next_y, next_dir, cost + 1))
					visited[next_x][next_y][next_dir] = True
					pre[next_x][next_y][next_dir] = prev_dir

	print("No")


if __name__ == "__main__":
	main()

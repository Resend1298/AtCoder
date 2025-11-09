# TODO: unsolved

from sortedcontainers import SortedKeyList


def solve():
	h, w = [int(i) for i in input().split()]
	s = [input() for _ in range(h)]

	edges = [[[[] for _ in range(4)] for _ in range(w)] for _ in range(h)]
	for i in range(h):
		for j in range(w):
			match s[i][j]:
				case 'A':
					# from up
					if i + 1 < h:
						edges[i][j][0].append((i + 1, j, 0))
					if 0 <= j - 1:
						edges[i][j][0].append((i, j - 1, 1))
					if j + 1 < w:
						edges[i][j][0].append((i, j + 1, 1))
					# from down
					if 0 <= i - 1:
						edges[i][j][1].append((i - 1, j, 0))
					if 0 <= j - 1:
						edges[i][j][1].append((i, j - 1, 1))
					if j + 1 < w:
						edges[i][j][1].append((i, j + 1, 1))
					# from left
					if j + 1 < w:
						edges[i][j][2].append((i, j + 1, 0))
					if 0 <= i - 1:
						edges[i][j][2].append((i - 1, j, 1))
					if i + 1 < h:
						edges[i][j][2].append((i + 1, j, 1))
					# from right
					if 0 <= j - 1:
						edges[i][j][3].append((i, j - 1, 0))
					if 0 <= i - 1:
						edges[i][j][3].append((i - 1, j, 1))
					if i + 1 < h:
						edges[i][j][3].append((i + 1, j, 1))
				case 'B':
					# from up
					if i + 1 < h:
						edges[i][j][0].append((i + 1, j, 1))
					if 0 <= j - 1:
						edges[i][j][0].append((i, j - 1, 1))
					if j + 1 < w:
						edges[i][j][0].append((i, j + 1, 0))
					# from down
					if 0 <= i - 1:
						edges[i][j][1].append((i - 1, j, 1))
					if 0 <= j - 1:
						edges[i][j][1].append((i, j - 1, 0))
					if j + 1 < w:
						edges[i][j][1].append((i, j + 1, 1))
					# from left
					if j + 1 < w:
						edges[i][j][2].append((i, j + 1, 1))
					if 0 <= i - 1:
						edges[i][j][2].append((i - 1, j, 1))
					if i + 1 < h:
						edges[i][j][2].append((i + 1, j, 0))
					# from right
					if 0 <= j - 1:
						edges[i][j][3].append((i, j - 1, 1))
					if 0 <= i - 1:
						edges[i][j][3].append((i - 1, j, 0))
					if i + 1 < h:
						edges[i][j][3].append((i + 1, j, 1))
				case 'C':
					# from up
					if i + 1 < h:
						edges[i][j][0].append((i + 1, j, 1))
					if 0 <= j - 1:
						edges[i][j][0].append((i, j - 1, 0))
					if j + 1 < w:
						edges[i][j][0].append((i, j + 1, 1))
					# from down
					if 0 <= i - 1:
						edges[i][j][1].append((i - 1, j, 1))
					if 0 <= j - 1:
						edges[i][j][1].append((i, j - 1, 1))
					if j + 1 < w:
						edges[i][j][1].append((i, j + 1, 0))
					# from left
					if j + 1 < w:
						edges[i][j][2].append((i, j + 1, 1))
					if 0 <= i - 1:
						edges[i][j][2].append((i - 1, j, 0))
					if i + 1 < h:
						edges[i][j][2].append((i + 1, j, 1))
					# from right
					if 0 <= j - 1:
						edges[i][j][3].append((i, j - 1, 1))
					if 0 <= i - 1:
						edges[i][j][3].append((i - 1, j, 1))
					if i + 1 < h:
						edges[i][j][3].append((i + 1, j, 0))

	q = SortedKeyList(key=lambda x: x[0])
	dis = [[[float("inf")] * 4 for _ in range(w)] for _ in range(h)]
	dis[0][0][2] = 0
	q.add((0, 0, 0, 2))
	visited = [[False] * w for _ in range(h)]

	while q:
		_, x, y, from_direction = q.pop(0)
		if visited[x][y]:
			continue
		visited[x][y] = True
		for newx, newy, cost in edges[x][y][from_direction]:
			if newx == x + 1 and newy == y:
				new_direction = 0
			elif newx == x - 1 and newy == y:
				new_direction = 1
			elif newx == x and newy == y + 1:
				new_direction = 2
			else:
				new_direction = 3
			if dis[newx][newy][new_direction] > dis[x][y][from_direction] + cost:
				dis[newx][newy][new_direction] = dis[x][y][from_direction] + cost
				q.add((dis[newx][newy][new_direction], newx, newy, new_direction))

	pass


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

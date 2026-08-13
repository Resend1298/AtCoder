from collections import defaultdict, deque
from string import ascii_lowercase


def main():
	h, w = [int(i) for i in input().split()]
	s = [input() for _ in range(h)]

	warp_cells = defaultdict(list)
	for i in range(h):
		for j in range(w):
			if s[i][j] in ascii_lowercase:
				warp_cells[s[i][j]].append((i, j))

	q = deque()
	visited = [[False] * w for _ in range(h)]
	visited_warp = {i: False for i in ascii_lowercase}
	q.append((0, 0, 0))
	visited[0][0] = True

	while q:
		x, y, cost = q.popleft()

		if (x, y) == (h - 1, w - 1):
			print(cost)
			exit()

		if s[x][y] in ascii_lowercase and not visited_warp[s[x][y]]:
			for new_x, new_y in warp_cells[s[x][y]]:
				if not visited[new_x][new_y]:
					q.append((new_x, new_y, cost + 1))
					visited[new_x][new_y] = True
			visited_warp[s[x][y]] = True

		for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
			if 0 <= new_x < h and 0 <= new_y < w and s[new_x][new_y] != '#' and not visited[new_x][new_y]:
				q.append((new_x, new_y, cost + 1))
				visited[new_x][new_y] = True

	print(-1)


if __name__ == "__main__":
	main()

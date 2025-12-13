from collections import deque, defaultdict


def main():
	h, w = [int(i) for i in input().split()]
	s = [input() for _ in range(h)]

	teleports = defaultdict(list)
	teleported = {chr(ord('a') + i): False for i in range(26)}
	for i in range(h):
		for j in range(w):
			if 'a' <= s[i][j] <= 'z':
				teleports[s[i][j]].append((i, j))

	q = deque()
	visited = [[False] * w for _ in range(h)]

	q.append((0, 0, 0))
	visited[0][0] = True

	while q:
		x, y, cost = q.popleft()

		if x == h - 1 and y == w - 1:
			print(cost)
			exit()

		if 'a' <= s[x][y] <= 'z' and not teleported[s[x][y]]:
			teleported[s[x][y]] = True
			for new_x, new_y in teleports[s[x][y]]:
				if not visited[new_x][new_y]:
					q.append((new_x, new_y, cost + 1))
					visited[new_x][new_y] = True

		for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
			if 0 <= new_x < h and 0 <= new_y < w and not visited[new_x][new_y] and s[new_x][new_y] != '#':
				q.append((new_x, new_y, cost + 1))
				visited[new_x][new_y] = True

	print(-1)


if __name__ == "__main__":
	main()

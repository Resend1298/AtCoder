from collections import deque


def main():
	h, w = [int(i) for i in input().split()]
	s = [input() for _ in range(h)]

	white = []
	for i in range(h):
		for j in range(w):
			if s[i][j] == '.':
				white.append((i, j))

	visited = [[False] * w for _ in range(h)]
	result = 0

	for i, j in white:
		if visited[i][j]:
			continue

		visited[i][j] = True
		q = deque([(i, j)])
		count = True

		while q:
			x, y = q.popleft()

			if x == 0 or x == h - 1 or y == 0 or y == w - 1:
				count = False

			for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
				if 0 <= new_x < h and 0 <= new_y < w and s[new_x][new_y] == '.' and not visited[new_x][new_y]:
					visited[new_x][new_y] = True
					q.append((new_x, new_y))

		if count:
			result += 1

	print(result)


if __name__ == "__main__":
	main()

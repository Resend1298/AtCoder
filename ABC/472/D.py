from collections import deque


def main():
	h, w, k = [int(i) for i in input().split()]
	s = [input() for _ in range(h)]

	safe_row = [True] * h
	safe_col = [True] * w
	for i in range(h):
		for j in range(w):
			if s[i][j] == '#':
				safe_row[i] = False
				safe_col[j] = False

	q = deque()
	visited = [[float("inf")] * w for _ in range(h)]

	for i in range(h):
		for j in range(w):
			if safe_row[i] and safe_col[j]:
				q.append((i, j, 0))
				visited[i][j] = 0

	while q:
		x, y, cost = q.popleft()

		for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
			if 0 <= new_x < h and 0 <= new_y < w and s[new_x][new_y] == '.' and visited[new_x][new_y] == float("inf"):
				q.append((new_x, new_y, cost + 1))
				visited[new_x][new_y] = cost + 1

	result = 0
	for i in range(h):
		for j in range(w):
			if visited[i][j] <= k:
				result += 1

	print(result)


if __name__ == "__main__":
	main()

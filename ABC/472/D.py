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
	cost = [[float("inf")] * w for _ in range(h)]

	for i in range(h):
		for j in range(w):
			if safe_row[i] and safe_col[j]:
				q.append((i, j, 0))
				cost[i][j] = 0

	while q:
		x, y, current_cost = q.popleft()

		for new_x, new_y in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
			if 0 <= new_x < h and 0 <= new_y < w and s[new_x][new_y] == '.' and cost[new_x][new_y] == float("inf"):
				q.append((new_x, new_y, current_cost + 1))
				cost[new_x][new_y] = current_cost + 1

	result = 0
	for i in range(h):
		for j in range(w):
			if cost[i][j] <= k:
				result += 1

	print(result)


if __name__ == "__main__":
	main()

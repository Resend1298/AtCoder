from collections import deque


def main():
	h, w = [int(i) for i in input().split()]
	a = [input() for _ in range(h)]

	for i in range(h):
		for j in range(w):
			if a[i][j] == 'S':
				sx, sy = i, j

	q = deque()
	visited = [[False] * w for _ in range(h)]
	visited_switch = [[False] * w for _ in range(h)]

	# noinspection PyUnboundLocalVariable
	q.append((sx, sy, 0, False))
	visited[sx][sy] = True

	while q:
		x, y, cost, switch = q.popleft()

		for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
			if 0 <= new_x < h and 0 <= new_y < w:
				if (not switch and not visited[new_x][new_y]) or (switch and not visited_switch[new_x][new_y]):
					match a[new_x][new_y]:
						case '.' | 'S':
							q.append((new_x, new_y, cost + 1, switch))
							if not switch:
								visited[new_x][new_y] = True
							else:
								visited_switch[new_x][new_y] = True
						case 'G':
							print(cost + 1)
							exit()
						case 'o' if not switch:
							q.append((new_x, new_y, cost + 1, switch))
							visited[new_x][new_y] = True
						case 'x' if switch:
							q.append((new_x, new_y, cost + 1, switch))
							visited_switch[new_x][new_y] = True
						case '?':
							q.append((new_x, new_y, cost + 1, not switch))
							if not switch:
								visited[new_x][new_y] = True
							else:
								visited_switch[new_x][new_y] = True
	else:
		print(-1)


if __name__ == "__main__":
	main()

# TODO: review

import heapq


def main():
	h, w = [int(i) for i in input().split()]
	a = [list(input()) for _ in range(h)]

	for i in range(h):
		for j in range(w):
			if a[i][j] == 'S':
				sx, sy = i, j
			if a[i][j] == 'G':
				gx, gy = i, j

	dis = [[float("inf")] * w for _ in range(h)]
	dis_toggle = [[float("inf")] * w for _ in range(h)]
	dis[sx][sy] = 0
	q = [(0, sx, sy, False)]
	vis = set()

	while q:
		_, x, y, toggle = heapq.heappop(q)
		if (x, y, toggle) in vis:
			continue
		vis.add((x, y, toggle))

		for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
			if 0 <= new_x < h and 0 <= new_y < w:
				if a[new_x][new_y] in ['.', 'S', 'G']:
					if not toggle and dis[new_x][new_y] > dis[x][y] + 1:
						dis[new_x][new_y] = dis[x][y] + 1
						heapq.heappush(q, (dis[new_x][new_y], new_x, new_y, False))
					elif toggle and dis_toggle[new_x][new_y] > dis_toggle[x][y] + 1:
						dis_toggle[new_x][new_y] = dis_toggle[x][y] + 1
						heapq.heappush(q, (dis_toggle[new_x][new_y], new_x, new_y, True))
				elif a[new_x][new_y] == '?':
					if not toggle and dis_toggle[new_x][new_y] > dis[x][y] + 1:
						dis_toggle[new_x][new_y] = dis[x][y] + 1
						heapq.heappush(q, (dis_toggle[new_x][new_y], new_x, new_y, True))
					elif toggle and dis[new_x][new_y] > dis_toggle[x][y] + 1:
						dis[new_x][new_y] = dis_toggle[x][y] + 1
						heapq.heappush(q, (dis[new_x][new_y], new_x, new_y, False))
				elif a[new_x][new_y] == 'o' and not toggle:
					if dis[new_x][new_y] > dis[x][y] + 1:
						dis[new_x][new_y] = dis[x][y] + 1
						heapq.heappush(q, (dis[new_x][new_y], new_x, new_y, False))
				elif a[new_x][new_y] == 'x' and toggle:
					if dis_toggle[new_x][new_y] > dis_toggle[x][y] + 1:
						dis_toggle[new_x][new_y] = dis_toggle[x][y] + 1
						heapq.heappush(q, (dis_toggle[new_x][new_y], new_x, new_y, True))

	if dis[gx][gy] == float("inf") and dis_toggle[gx][gy] == float("inf"):
		print(-1)
	else:
		print(min(dis[gx][gy], dis_toggle[gx][gy]))


if __name__ == "__main__":
	main()

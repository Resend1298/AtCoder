# TODO: review

from collections import deque


def main():
	n, m, l, s, t = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		u, v, c = [int(i) for i in input().split()]
		edges[u - 1].append((v - 1, c))

	q = deque()
	visited = [[set() for _ in range(l + 1)] for _ in range(n)]

	q.append((0, 0, 0))
	visited[0][0].add(0)

	result = set()

	while q:
		current, count, cost = q.popleft()

		if count == l and s <= cost <= t:
			result.add(current + 1)
			continue

		if count < l and cost < t:
			for i, j in edges[current]:
				if cost + j not in visited[i][count + 1]:
					q.append((i, count + 1, cost + j))
					visited[i][count + 1].add(cost + j)

	result = sorted(result)
	print(*result)


if __name__ == "__main__":
	main()

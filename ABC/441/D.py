from collections import deque


def main():
	n, m, l, s, t = [int(i) for i in input().split()]
	# noinspection DuplicatedCode
	edges = [[] for _ in range(n)]
	for _ in range(m):
		u, v, c = [int(i) for i in input().split()]
		edges[u - 1].append((v - 1, c))

	q = deque()
	q.append((0, 0, 0))
	result = set()

	while q:
		current, edge_count, cost = q.popleft()

		if edge_count == l and s <= cost <= t:
			result.add(current + 1)
			continue
		if edge_count >= l or cost >= t:
			continue

		for i, j in edges[current]:
			q.append((i, edge_count + 1, cost + j))

	print(*sorted(result))


if __name__ == "__main__":
	main()

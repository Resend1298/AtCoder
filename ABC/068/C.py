from collections import deque


def main():
	# noinspection DuplicatedCode
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		a, b = [int(i) - 1 for i in input().split()]
		edges[a].append(b)
		edges[b].append(a)

	q = deque()
	visited = [False] * n
	q.append((0, 0))
	visited[0] = True

	while q:
		current, cost = q.popleft()

		if cost >= 2:
			break

		for i in edges[current]:
			if not visited[i]:
				q.append((i, cost + 1))
				visited[i] = True

	if visited[n - 1]:
		print("POSSIBLE")
	else:
		print("IMPOSSIBLE")


if __name__ == "__main__":
	main()

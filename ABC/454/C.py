from collections import deque


def main():
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		a, b = [int(i) - 1 for i in input().split()]
		edges[a].append(b)

	q = deque([0])
	visited = [False] * n
	visited[0] = True

	while q:
		current = q.popleft()

		for i in edges[current]:
			if not visited[i]:
				q.append(i)
				visited[i] = True

	print(visited.count(True))


if __name__ == "__main__":
	main()

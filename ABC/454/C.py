# TODO: review

from collections import deque


def main():
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		a, b = [int(i) - 1 for i in input().split()]
		edges[a].append(b)

	visited = [False] * n
	q = deque()
	visited[0] = True
	q.append(0)

	while q:
		current = q.popleft()

		for i in edges[current]:
			if not visited[i]:
				visited[i] = True
				q.append(i)

	print(visited.count(True))


if __name__ == "__main__":
	main()

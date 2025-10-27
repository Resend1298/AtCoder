from collections import deque


def main():
	n, m = [int(i) for i in input().split()]
	edges: list[list[int]] = [[] for _ in range(n)]
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edges[u].append(v)
		edges[v].append(u)
	s = input()
	safe = {i for i in range(n) if s[i] == "S"}
	danger = {i for i in range(n) if s[i] == "D"}

	q = deque()
	visited = [set() for _ in range(n)]
	result = [0] * n

	for i in safe:
		q.append((i, 0, i))
		visited[i].add(i)

	while q:
		v, cost, origin = q.popleft()

		if v in danger:
			result[v] += cost

		for i in edges[v]:
			if len(visited[i]) < 2 and origin not in visited[i]:
				q.append((i, cost + 1, origin))
				visited[i].add(origin)

	for i in sorted(danger):
		print(result[i])


if __name__ == "__main__":
	main()

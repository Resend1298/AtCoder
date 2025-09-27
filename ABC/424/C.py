from collections import deque


def main():
	n = int(input())

	q = deque()
	visited = [False] * n
	edges: list[list[int]] = [[] for _ in range(n)]

	for i in range(n):
		a, b = [int(i) - 1 for i in input().split()]

		if a == -1 and b == -1:
			q.append(i)
			visited[i] = True
		elif a == b:
			edges[a].append(i)
		else:
			edges[a].append(i)
			edges[b].append(i)

	while q:
		tmp = q.popleft()

		for i in edges[tmp]:
			if not visited[i]:
				q.append(i)
				visited[i] = True

	print(visited.count(True))


if __name__ == "__main__":
	main()

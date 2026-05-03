from collections import deque


def main():
	n, m = [int(i) for i in input().split()]
	edges: list[list[int]] = [[] for _ in range(n)]
	for _ in range(m):
		x, y = [int(i) - 1 for i in input().split()]
		edges[y].append(x)

	bfs_q = deque()
	visited = [False] * n

	q = int(input())
	for _ in range(q):
		match [int(i) - 1 for i in input().split()]:
			case [0, v]:
				if not visited[v]:
					bfs_q.append(v)
					visited[v] = True
			case [1, v]:
				if visited[v]:
					print("Yes")
					continue

				while bfs_q:
					tmp = bfs_q.popleft()
					for i in edges[tmp]:
						if not visited[i]:
							bfs_q.append(i)
							visited[i] = True

				print("Yes" if visited[v] else "No")


if __name__ == "__main__":
	main()

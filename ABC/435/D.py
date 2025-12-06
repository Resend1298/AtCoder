from collections import deque


def main():
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		x, y = [int(i) - 1 for i in input().split()]
		edges[y].append(x)

	q = deque()
	visited = [False] * n

	q_count = int(input())
	for _ in range(q_count):
		match [int(i) for i in input().split()]:
			case [1, v]:
				v -= 1
				if not visited[v]:
					visited[v] = True
					q.append(v)
			case [2, v]:
				v -= 1

				if visited[v]:
					print("Yes")
					continue

				while q:
					tmp = q.popleft()
					for i in edges[tmp]:
						if not visited[i]:
							visited[i] = True
							q.append(i)

				print("Yes" if visited[v] else "No")


if __name__ == "__main__":
	main()

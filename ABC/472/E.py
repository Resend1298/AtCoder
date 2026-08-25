from sys import setrecursionlimit


def solve():
	# noinspection DuplicatedCode
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		a, b = [int(i) - 1 for i in input().split()]
		edges[a].append(b)
		edges[b].append(a)

	visited = [float("inf")] * n
	path = []

	def dfs(node, cost: int):
		visited[node] = cost
		path.append(node + 1)

		for i in edges[node]:
			if visited[i] <= cost - 2 and (cost - visited[i]) % 2 == 0:
				start_index = path.index(i + 1)
				print(len(path) - start_index)
				print(*path[start_index:])
				return True

			if visited[i] == float("inf"):
				if dfs(i, cost + 1):
					return True

		path.pop()
		return False

	setrecursionlimit(10 ** 7)
	if not dfs(0, 0):
		print(-1)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

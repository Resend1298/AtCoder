import sys


def solve():
	n, m, x, y = [int(i) for i in input().split()]
	x -= 1
	y -= 1
	edges = [[] for _ in range(n)]
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edges[u].append(v)
		edges[v].append(u)

	for i in edges:
		i.sort()
	visited = [False] * n
	path = []
	finished = False

	def dfs(i):
		nonlocal finished

		if i == y:
			path.append(i + 1)
			print(*path)
			finished = True
			return

		visited[i] = True
		path.append(i + 1)

		for j in edges[i]:
			if not visited[j]:
				dfs(j)
				if finished:
					return

		path.pop()

	sys.setrecursionlimit(10 ** 7)
	dfs(x)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

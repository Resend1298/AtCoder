# TODO: review

def solve():
	n, m, x, y = [int(i) for i in input().split()]
	x -= 1
	y -= 1
	edge = [[] for _ in range(n)]
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edge[u].append(v)
		edge[v].append(u)

	for i in edge:
		i.sort()

	visited = [False] * n
	path = []
	finished = False

	def dfs(i):
		if i == y:
			path.append(i + 1)
			print(*path)
			nonlocal finished
			finished = True
			return

		visited[i] = True
		path.append(i + 1)

		for j in edge[i]:
			if not visited[j]:
				dfs(j)
				if finished:
					return

		path.pop()

	dfs(x)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

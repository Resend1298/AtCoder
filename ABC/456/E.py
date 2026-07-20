from sys import setrecursionlimit


def solve():
	n, m = [int(i) for i in input().split()]
	edges = [[i] for i in range(n)]
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edges[u].append(v)
		edges[v].append(u)
	w = int(input())
	s = [input() for _ in range(n)]

	possible: list[list[bool | None]] = [[None] * w for _ in range(n)]

	def dfs(i, day):
		possible[i][day] = True

		for j in edges[i]:
			if possible[j][(day + 1) % w]:
				print("Yes")
				return True
			if possible[j][(day + 1) % w] is None and s[j][(day + 1) % w] == 'o':
				if dfs(j, (day + 1) % w):
					return True

		possible[i][day] = False
		return False

	setrecursionlimit(10 ** 7)
	for i in range(n):
		if s[i][0] == 'o':
			if dfs(i, 0):
				return
	print("No")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

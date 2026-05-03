# TODO: review

from sys import setrecursionlimit


def solve():
	n, m = [int(i) for i in input().split()]
	edges = [[] for _ in range(n)]
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edges[u].append(v)
		edges[v].append(u)
	w = int(input())
	s = [input() for _ in range(n)]

	start = [i for i in range(n) if s[i][0] == 'o']
	if not start:
		print("No")
		return

	possible = [[0] * w for _ in range(n)]

	# 0: Unknown, 1: possible, 2: impossible

	def dfs(i, current_w):
		possible[i][current_w] = 1

		next_w = current_w + 1 if current_w != w - 1 else 0
		if s[i][next_w] == 'o':
			if possible[i][next_w] == 1:
				print("Yes")
				return True
			elif possible[i][next_w] == 0:
				if dfs(i, next_w):
					return True
		for j in edges[i]:
			if s[j][next_w] == 'o':
				if possible[j][next_w] == 1:
					print("Yes")
					return True
				elif possible[j][next_w] == 0:
					if dfs(j, next_w):
						return True

		possible[i][current_w] = 2
		return False

	setrecursionlimit(10 ** 7)
	for i in start:
		if possible[i][0] != 2:
			if dfs(i, 0):
				return
	print("No")


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

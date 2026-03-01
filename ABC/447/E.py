# noinspection DuplicatedCode
class UnionFind:
	def __init__(self, n):
		self._parent = [i for i in range(n)]
		self._size = [1] * n

		self.connected_count = n

	def find(self, x):
		if self._parent[x] == x:
			return x

		self._parent[x] = self.find(self._parent[x])
		return self._parent[x]

	def union(self, x, y):
		x = self.find(x)
		y = self.find(y)

		if x == y:
			return

		if self._size[x] < self._size[y]:
			x, y = y, x
		self._parent[y] = x
		self._size[x] += self._size[y]

		self.connected_count -= 1


def main():
	n, m = [int(i) for i in input().split()]
	edges = [[int(i) - 1 for i in input().split()] for _ in range(m)]

	uf = UnionFind(n)
	result = 0

	cost = [1]
	for i in range(1, m + 1):
		cost.append((cost[-1] * 2) % 998244353)

	for i in range(m - 1, -1, -1):
		u, v = edges[i]

		if uf.connected_count > 2:
			uf.union(u, v)
		elif uf.find(u) != uf.find(v):
			result = (result + cost[i + 1]) % 998244353

	print(result)


if __name__ == "__main__":
	main()

from collections import Counter


# noinspection DuplicatedCode
class UnionFind:
	def __init__(self, n):
		self._parent = [i for i in range(n)]
		self._size = [1] * n

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


def main():
	n, k, l = [int(i) for i in input().split()]

	road = UnionFind(n)
	rail = UnionFind(n)

	for _ in range(k):
		p, q = [int(i) - 1 for i in input().split()]
		road.union(p, q)
	for _ in range(l):
		r, s = [int(i) - 1 for i in input().split()]
		rail.union(r, s)

	root_pair = [(road.find(i), rail.find(i)) for i in range(n)]
	root_pair_count = Counter(root_pair)
	print(*[root_pair_count[i] for i in root_pair])


if __name__ == "__main__":
	main()

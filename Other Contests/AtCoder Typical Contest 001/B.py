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

	def connected(self, x, y):
		return self.find(x) == self.find(y)


def main():
	n, q = [int(i) for i in input().split()]

	uf = UnionFind(n)

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case [0, a, b]:
				uf.union(a, b)
			case [1, a, b]:
				print("Yes" if uf.connected(a, b) else "No")


if __name__ == "__main__":
	main()

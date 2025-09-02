# noinspection DuplicatedCode
class UnionFind:
	def __init__(self, n):
		self._parent = [i for i in range(n)]
		self._size = [1] * n

		self._color = ["white"] * n
		self._black_count = [0] * n

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

		self._black_count[x] += self._black_count[y]

	def change_color(self, x):
		match self._color[x]:
			case "white":
				self._color[x] = "black"
				self._black_count[self.find(x)] += 1
			case "black":
				self._color[x] = "white"
				self._black_count[self.find(x)] -= 1

	def black_reachable(self, x):
		return self._black_count[self.find(x)] > 0


def main():
	n, q = [int(i) for i in input().split()]

	uf = UnionFind(n)

	for _ in range(q):
		query = [int(i) for i in input().split()]

		match query[0]:
			case 1:
				u = query[1] - 1
				v = query[2] - 1
				uf.union(u, v)
			case 2:
				v = query[1] - 1
				uf.change_color(v)
			case 3:
				v = query[1] - 1
				print("Yes" if uf.black_reachable(v) else "No")


if __name__ == "__main__":
	main()

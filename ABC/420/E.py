class UnionFind:
	def __init__(self, size):
		self.parent = list(range(size))
		self.black_count = [0] * size

	def find(self, i):
		# If i itself is root or representative
		if self.parent[i] == i:
			return i

		# Else recursively find the representative
		# of the parent
		return self.find(self.parent[i])

	def unite(self, i, j):
		# Representative of set containing i
		irep = self.find(i)

		# Representative of set containing j
		jrep = self.find(j)

		if irep != jrep:
			self.parent[max(irep, jrep)] = min(irep, jrep)
			self.black_count[min(irep, jrep)] += self.black_count[max(irep, jrep)]

	def black(self, i):
		irep = self.find(i)
		self.black_count[irep] += 1

	def white(self, i):
		irep = self.find(i)
		self.black_count[irep] -= 1

	def connected_black(self, i):
		irep = self.find(i)
		return True if self.black_count[irep] > 0 else False


def main():
	n, q = [int(i) for i in input().split()]

	uf = UnionFind(n)
	color = ['w'] * n

	for _ in range(q):
		query = [int(i) for i in input().split()]

		match query[0]:
			case 1:
				x, y = query[1] - 1, query[2] - 1
				uf.unite(x, y)
			case 2:
				u = query[1] - 1
				if color[u] == 'w':
					color[u] = 'b'
					uf.black(u)
				else:
					color[u] = 'w'
					uf.white(u)
			case 3:
				u = query[1] - 1
				if uf.connected_black(u):
					print("Yes")
				else:
					print("No")


if __name__ == "__main__":
	main()

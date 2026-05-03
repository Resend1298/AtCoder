# CPython TLE, PyPy AC

# noinspection DuplicatedCode
class SegmentTree:
	def __init__(self, combine_func, default_node_value, array):
		"""
		:param default_node_value: combine_func(x, default_node_value) == x for any x
		"""

		self._n = len(array)
		self._combine_func = combine_func
		self._default_node_value = default_node_value

		self._leaf_size = 1
		while self._leaf_size < self._n:
			self._leaf_size *= 2

		self._nodes = [self._default_node_value for _ in range(self._leaf_size * 2)]

		self._build(array)

	def _build(self, array):
		for i in range(self._n):
			self._nodes[self._leaf_size + i] = array[i]
		for i in range(self._leaf_size - 1, 0, -1):
			self._nodes[i] = self._combine_func(self._nodes[i * 2], self._nodes[i * 2 + 1])

	def update(self, index, value):
		index += self._leaf_size
		self._nodes[index] = value
		while index > 1:
			index //= 2
			self._nodes[index] = self._combine_func(self._nodes[index * 2], self._nodes[index * 2 + 1])

	def query(self, left, right):
		"""
		[left, right)
		"""

		left += self._leaf_size
		right += self._leaf_size
		result_left = self._default_node_value
		result_right = self._default_node_value

		while left < right:
			if left % 2 == 1:
				result_left = self._combine_func(result_left, self._nodes[left])
				left += 1
			if right % 2 == 1:
				right -= 1
				result_right = self._combine_func(self._nodes[right], result_right)
			left //= 2
			right //= 2

		return self._combine_func(result_left, result_right)


def main():
	n, q = [int(i) for i in input().split()]
	xy = [[int(i) for i in input().split()] for _ in range(n)]

	xy_distances = [(x + y, x - y, -x + y, -x - y) for x, y in xy]
	seg_tree = SegmentTree(lambda a, b: [max(i, j) for i, j in zip(a, b)], [float("-inf")] * 4, xy_distances)

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, i, x, y:
				seg_tree.update(i - 1, (x + y, x - y, -x + y, -x - y))
			case 2, l, r, x, y:
				tree_distances = seg_tree.query(l - 1, r)
				coordinate_distances = (-x - y, -x + y, x - y, x + y)
				print(max(i + j for i, j in zip(tree_distances, coordinate_distances)))


if __name__ == "__main__":
	main()

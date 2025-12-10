from sys import setrecursionlimit


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


def search(current_index, left_index, right_index, p_value_to_index, seg_tree):
	if left_index < current_index < right_index:
		max_left = seg_tree.query(left_index, current_index)
		max_left_index = p_value_to_index[max_left]
		max_right = seg_tree.query(current_index + 1, right_index + 1)
		max_right_index = p_value_to_index[max_right]
		return max(
			current_index - max_left_index + search(max_left_index, left_index, current_index - 1, p_value_to_index,
			                                        seg_tree),
			max_right_index - current_index + search(max_right_index, current_index + 1, right_index, p_value_to_index,
			                                         seg_tree))
	elif left_index == right_index:
		return 0
	elif current_index == left_index:
		max_right = seg_tree.query(current_index + 1, right_index + 1)
		max_right_index = p_value_to_index[max_right]
		return max_right_index - current_index + search(max_right_index, current_index + 1, right_index,
		                                                p_value_to_index, seg_tree)
	else:  # current_index==right_index
		max_left = seg_tree.query(left_index, current_index)
		max_left_index = p_value_to_index[max_left]
		return current_index - max_left_index + search(max_left_index, left_index, current_index - 1, p_value_to_index,
		                                               seg_tree)


def main():
	n = int(input())
	p = [int(i) for i in input().split()]

	p_value_to_index = {p[i]: i for i in range(n)}
	seg_tree = SegmentTree(max, float("-inf"), p)

	setrecursionlimit(10 ** 7)
	print(search(p_value_to_index[n], 0, n - 1, p_value_to_index, seg_tree))


if __name__ == "__main__":
	main()

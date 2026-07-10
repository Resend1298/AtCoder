# CPython TLE, PyPy AC

from bisect import bisect_right
from collections import deque


def main():
	s = input()
	t = input()

	s_char_index = [[] for _ in range(26)]
	for i, c in enumerate(s):
		s_char_index[ord(c) - ord('a')].append(i)

	min_necessary_range = deque()
	for start in s_char_index[ord(t[0]) - ord('a')]:
		current_index = start
		for t_char in t[1:]:
			next_index_index = bisect_right(s_char_index[ord(t_char) - ord('a')], current_index)
			if next_index_index == len(s_char_index[ord(t_char) - ord('a')]):
				break
			current_index = s_char_index[ord(t_char) - ord('a')][next_index_index]
		else:
			min_necessary_range.append((start, current_index))

	result = len(s) * (len(s) + 1) // 2
	for l in range(len(s)):
		while min_necessary_range and min_necessary_range[0][0] < l:
			min_necessary_range.popleft()
		if not min_necessary_range:
			break

		result -= len(s) - min_necessary_range[0][1]

	print(result)


if __name__ == "__main__":
	main()

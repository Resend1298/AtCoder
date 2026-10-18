from collections import defaultdict
from string import ascii_lowercase


def main():
	n, m = [int(i) for i in input().split()]
	s = [input() for _ in range(n)]
	t = [input() for _ in range(m)]

	result = [0] * n
	name_to_index = {name: index for index, name in enumerate(s)}
	name_to_index_fuzzy = defaultdict(set)

	for index, name in enumerate(s):
		for change_index in range(len(name)):
			for char in ascii_lowercase:
				name_to_index_fuzzy[name[:change_index] + char + name[change_index + 1:]].add(index)

	for name in t:
		if name in name_to_index:
			result[name_to_index[name]] += 1
		elif len(name_to_index_fuzzy[name]) == 1:
			result[next(iter(name_to_index_fuzzy[name]))] += 1

	for i in result:
		print(i)


if __name__ == "__main__":
	main()

from collections import defaultdict
from sys import setrecursionlimit


def search(ab, current_index, max_used, saved):
	if (current_index, max_used) in saved:
		return saved[(current_index, max_used)]

	if current_index >= len(ab):
		saved[(current_index, max_used)] = 0
		return 0

	a, b = ab[current_index]
	if b > max_used:
		saved[(current_index, max_used)] = max(
			search(ab, current_index + 1, max_used, saved),
			search(ab, current_index + 1, b, saved) + 1
		)
		return saved[(current_index, max_used)]
	else:
		saved[(current_index, max_used)] = search(ab, current_index + 1, max_used, saved)
		return saved[(current_index, max_used)]


def main():
	n = int(input())
	ab = [[int(i) for i in input().split()] for _ in range(n)]

	ab_dict = defaultdict(lambda: float("inf"))
	for a, b in ab:
		ab_dict[a] = min(ab_dict[a], b)
	ab = sorted(ab_dict.items())

	setrecursionlimit(10 ** 7)
	saved = {}
	print(search(ab, 0, -1, saved))


if __name__ == "__main__":
	main()

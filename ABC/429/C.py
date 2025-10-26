# TODO: review

from collections import defaultdict


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	counter = defaultdict(list)
	for i in range(n):
		counter[a[i]].append(i)

	result = 0

	for value in counter.values():
		if len(value) < 2:
			continue

		lenv = len(value)

		result += lenv * (lenv - 1) // 2 * (n - lenv)

	print(result)


if __name__ == "__main__":
	main()

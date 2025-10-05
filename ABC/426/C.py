# TODO: TLE

from sortedcontainers import SortedKeyList


def main():
	n, q = [int(i) for i in input().split()]

	sum_count = [i for i in range(1, n + 1)]
	min_version = 0
	minus = SortedKeyList(key=lambda x: x[0])

	for _ in range(q):
		x, y = [int(i) for i in input().split()]

		if x < min_version:
			print(0)
			continue
		min_version = x + 1

		start = minus.bisect_key_left(x)
		result = sum_count[x - 1]
		if start != len(minus):
			for i in range(start, len(minus)):
				result -= minus[i][1]
		print(result)
		minus.add((y - 1, result))


if __name__ == "__main__":
	main()

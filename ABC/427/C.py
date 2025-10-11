from itertools import combinations


def main():
	n, m = [int(i) for i in input().split()]
	edges = []
	for _ in range(m):
		u, v = [int(i) - 1 for i in input().split()]
		edges.append((u, v))

	result = float("inf")

	for i in range(1, n // 2 + 1):
		for j in combinations(range(n), i):
			tmp_result = 0
			for x, y in edges:
				if (x in j and y in j) or (x not in j and y not in j):
					tmp_result += 1
			result = min(result, tmp_result)

	print(result)


if __name__ == "__main__":
	main()

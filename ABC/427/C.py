from itertools import combinations


def main():
	n, m = [int(i) for i in input().split()]
	edges = [[int(i) - 1 for i in input().split()] for _ in range(m)]

	result = float("inf")

	for smaller_set_size in range(1, n // 2 + 1):
		for smaller_set in combinations(range(n), smaller_set_size):
			tmp_result = 0

			for u, v in edges:
				if (u in smaller_set and v in smaller_set) or (u not in smaller_set and v not in smaller_set):
					tmp_result += 1

			result = min(result, tmp_result)

	print(result)


if __name__ == "__main__":
	main()

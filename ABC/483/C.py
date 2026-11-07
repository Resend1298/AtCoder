from collections import defaultdict


def main():
	n, m = [int(i) for i in input().split()]
	a, b = [], []
	for _ in range(m):
		tmp_a, tmp_b = [int(i) - 1 for i in input().split()]
		a.append(tmp_a)
		b.append(tmp_b)

	first = [0] * n
	second = [defaultdict(int) for _ in range(n)]
	for a, b in zip(a, b):
		first[a] += 1
		second[a][b] += 1
	max_1, max_1_count = 0, 0
	max_2, max_2_count = 0, 0
	for i in range(n):
		if first[i] > max_1_count:
			max_1 = i
			max_1_count = first[i]
	for i in range(n):
		if first[i] > max_2_count and i != max_1:
			max_2 = i
			max_2_count = first[i]

	for i in range(n):
		if i != max_1:
			current_max, current_max_count = max_1, max_1_count
		else:
			current_max, current_max_count = max_2, max_2_count
		for j, k in second[i].items():
			if (first[j] + k > current_max_count and j != i) or (
					first[j] + k >= current_max_count and j != i and j < current_max):
				current_max = j
				current_max_count = first[j] + k
		print(current_max + 1)


if __name__ == "__main__":
	main()

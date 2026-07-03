from collections import Counter


def main():
	n, x = [int(i) for i in input().split()]
	w = [int(input()) for _ in range(n)]

	w_1 = w[:n // 2]
	w_2 = w[n // 2:]

	count_1 = Counter()
	for i in range(2 ** len(w_1)):
		count_1[sum(w_1[j] for j in range(len(w_1)) if 2 ** j & i)] += 1

	count_2 = Counter()
	for i in range(2 ** len(w_2)):
		count_2[sum(w_2[j] for j in range(len(w_2)) if 2 ** j & i)] += 1

	result = 0
	for k, v in count_1.items():
		result += v * count_2[x - k]
	print(result)


if __name__ == "__main__":
	main()

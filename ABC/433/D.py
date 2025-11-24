from collections import Counter


def main():
	n, m = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	min_len = len(str(min(a)))
	max_len = len(str(max(a)))
	result = 0

	mod_results = {}
	for i in range(min_len, max_len + 1):
		mod_results[i] = Counter(-j % m for j in a if len(str(j)) == i)

	for i in a:
		for j in range(min_len, max_len + 1):
			result += mod_results[j][i * 10 ** j % m]

	print(result)


if __name__ == "__main__":
	main()

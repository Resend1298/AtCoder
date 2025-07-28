from itertools import product


def main():
	n, k, x = [int(i) for i in input().split()]
	s = [input() for _ in range(n)]

	all_combinations = []
	for i in product(range(n), repeat=k):
		f = ''.join([s[j] for j in i])
		all_combinations.append(f)

	all_combinations.sort()
	print(all_combinations[x - 1])


if __name__ == "__main__":
	main()

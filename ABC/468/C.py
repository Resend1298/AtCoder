from itertools import permutations


def main():
	n = int(input())
	p = tuple([int(i) for i in input().split()])
	q = tuple([int(i) for i in input().split()])

	result = 0

	for i in permutations(range(1, n + 1), n):
		if p < i < q:
			result += 1

	print(result)


if __name__ == "__main__":
	main()

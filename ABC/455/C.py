from collections import Counter


def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	sum_by_value = Counter()
	for i in a:
		sum_by_value[i] += i
	sum_by_value = sorted(sum_by_value.values(), reverse=True)

	if k >= len(sum_by_value):
		print(0)
		exit()

	print(sum(sum_by_value[k:]))


if __name__ == "__main__":
	main()

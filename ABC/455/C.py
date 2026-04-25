from collections import defaultdict


def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	sum_dict = defaultdict(int)
	sum_all = 0
	for i in a:
		sum_dict[i] += i
		sum_all += i
	sum_list = sorted(sum_dict.values(), reverse=True)

	for i in range(min(k, len(sum_list))):
		sum_all -= sum_list[i]

	print(sum_all)


if __name__ == "__main__":
	main()

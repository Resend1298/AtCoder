from bisect import bisect_left


def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) - 1 for i in input().split()]

	classes = [0] * k
	for i in a:
		classes[i] += 1
	classes.sort()

	min_possible_index = bisect_left(classes, classes[-1] - 1)
	print(k - min_possible_index)


if __name__ == "__main__":
	main()

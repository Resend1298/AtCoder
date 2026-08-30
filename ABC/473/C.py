# TODO: review

from bisect import bisect_left


def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) - 1 for i in input().split()]

	classes = [0] * k
	for i in a:
		classes[i] += 1
	classes.sort()

	max_people = classes[-1]
	target_index = bisect_left(classes, max_people - 1)

	print(k - target_index)


if __name__ == "__main__":
	main()

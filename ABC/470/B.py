# TODO: review

from collections import Counter


def main():
	n = int(input())
	c = [int(i) for i in input().split()]

	c_counter = Counter(c)
	max_count = c_counter.most_common(1)[0][1]
	print(n - max_count)


if __name__ == "__main__":
	main()

from collections import Counter


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	a_counter = Counter(a)
	a_sum = sum(a)

	for k, v in a_counter.items():
		if v >= 2:
			if v % 2 == 0:
				a_sum -= k * v
			else:
				a_sum -= k * (v - 1)

	print(a_sum)


if __name__ == "__main__":
	main()

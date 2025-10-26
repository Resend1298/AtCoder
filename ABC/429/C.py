from collections import Counter


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	a_counter = Counter(a)
	result = 0

	for i in a_counter.values():
		if i >= 2:
			result += i * (i - 1) // 2 * (n - i)

	print(result)


if __name__ == "__main__":
	main()

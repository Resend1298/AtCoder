from collections import Counter


def main():
	_ = int(input())
	a = [int(i) for i in input().split()]

	a_counter = Counter(a)
	result = 0

	for k, v in a_counter.items():
		result += k * (v % 2)

	print(result)


if __name__ == "__main__":
	main()

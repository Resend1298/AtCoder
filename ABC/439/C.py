# TODO: review

from collections import Counter


def main():
	n = int(input())

	max_x = int((n / 2) ** 0.5)
	result = Counter()
	for x in range(1, max_x + 1):
		for y in range(x + 1, n + 1):
			if x ** 2 + y ** 2 > n:
				break
			result[x ** 2 + y ** 2] += 1

	result = [k for k, v in result.items() if v == 1]
	result.sort()
	print(len(result))
	print(*result)


if __name__ == "__main__":
	main()

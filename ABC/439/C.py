# CPython TLE, PyPy AC

from collections import Counter


def main():
	n = int(input())

	max_x = int((n / 2) ** 0.5)
	counter = Counter()

	for x in range(1, max_x + 1):
		for y in range(x + 1, int((n - x ** 2) ** 0.5) + 1):
			counter[x ** 2 + y ** 2] += 1

	result = sorted(k for k, v in counter.items() if v == 1)
	print(len(result))
	print(*result)


if __name__ == "__main__":
	main()

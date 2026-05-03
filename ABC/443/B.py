from math import ceil


def main():
	n, k = [int(i) for i in input().split()]

	print(ceil((-2 * n - 1 + (4 * n ** 2 - 4 * n + 8 * k + 1) ** 0.5) / 2))


if __name__ == "__main__":
	main()

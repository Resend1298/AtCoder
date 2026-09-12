from math import ceil


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	coin_1, coin_10, coin_100 = 0, 0, 0

	for i in a:
		change = ceil(i / 1000) * 1000 - i
		coin_100 += change // 100
		change %= 100
		coin_10 += change // 10
		change %= 10
		coin_1 += change

	print(coin_1, coin_10, coin_100)


if __name__ == "__main__":
	main()

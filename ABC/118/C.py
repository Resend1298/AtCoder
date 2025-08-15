from math import gcd


def main():
	_ = int(input())
	a = [int(i) for i in input().split()]

	print(gcd(*a))


if __name__ == "__main__":
	main()

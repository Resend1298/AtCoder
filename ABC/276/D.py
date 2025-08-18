from math import gcd


def main():
	_ = int(input())
	a = [int(i) for i in input().split()]

	a_gcd = gcd(*a)
	result = 0

	for i in a:
		tmp = i // a_gcd

		while tmp != 1 and tmp % 2 == 0:
			tmp //= 2
			result += 1
		while tmp != 1 and tmp % 3 == 0:
			tmp //= 3
			result += 1

		if tmp != 1:
			print(-1)
			exit()

	print(result)


if __name__ == "__main__":
	main()

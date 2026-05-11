# TODO: review

from sys import setrecursionlimit


def recursion(current_index, p, n):
	if current_index == n:
		return 1

	if p[current_index] != current_index + 1:
		return 0

	return ((n - current_index - 1) + recursion(current_index + 1, p, n)) % 998244353


def solve():
	n = int(input())
	p = [int(i) for i in input().split()]

	setrecursionlimit(10 ** 7)
	result = recursion(0, p, n)
	print(result % 998244353)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

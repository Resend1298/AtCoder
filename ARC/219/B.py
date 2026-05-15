from sys import setrecursionlimit


def recursion(p, n, index):
	if p[index] != index + 1:
		return 0

	if index != n - 1:
		return n - index - 1 + recursion(p, n, index + 1)
	else:
		return 1


def solve():
	n = int(input())
	p = [int(i) for i in input().split()]

	setrecursionlimit(10 ** 7)
	print(recursion(p, n, 0) % 998244353)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

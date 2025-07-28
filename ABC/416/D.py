from sortedcontainers import SortedList


def solve():
	n, m = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	a = SortedList(a)
	b.sort(reverse=True)
	result = 0

	for i in range(n):
		target = a.bisect_left(m - b[i])
		if target != len(a):
			result += a[target] + b[i] - m
			del a[target]
		else:
			result += sum(a) + sum(b[i:])
			break

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

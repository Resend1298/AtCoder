# TODO: review

from sortedcontainers import SortedList


def solve():
	n, m = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	b.sort(reverse=True)
	a = SortedList(a)
	result = 0

	for i in range(n):
		target = a.bisect_left(m - b[i])
		if target != len(a):
			result += (b[i] + a[target]) % m
			a.remove(a[target])
		else:
			for j in range(i, n):
				result += b[j]
			result += sum(a)
			break

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

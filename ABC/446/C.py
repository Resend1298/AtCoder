# TODO: review

from collections import deque


def solve():
	n, d = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	q = deque()

	for i in range(n):
		q.append([i, a[i]])
		while b[i] > 0:
			tmp = min(b[i], q[0][1])
			b[i] -= tmp
			q[0][1] -= tmp
			if q[0][1] == 0:
				q.popleft()
		while q and q[0][0] + d <= i:
			q.popleft()

	print(sum(i[1] for i in q))


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

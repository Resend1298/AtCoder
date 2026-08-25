from collections import deque


def main():
	n, m, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	q = deque()
	q_sum = 0

	for i in range(1, n + 1):
		start = max(i - m + 1, 1) - 1

		while q and q[0][0] < start:
			q_sum -= q.popleft()[1]

		if a[i - 1] + q_sum <= k:
			print("Yes")
			q.append((i - 1, a[i - 1]))
			q_sum += a[i - 1]
		else:
			print("No")


if __name__ == "__main__":
	main()

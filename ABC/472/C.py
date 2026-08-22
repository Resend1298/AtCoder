from collections import deque


def main():
	n, m, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	q = deque()
	current_sum = 0

	for i in range(n):
		start = max(i + 1 - m + 1, 1) - 1
		while q and q[0][0] < start:
			current_sum -= q.popleft()[1]

		if current_sum + a[i] <= k:
			print("Yes")
			current_sum += a[i]
			q.append((i, a[i]))
		else:
			print("No")


if __name__ == "__main__":
	main()

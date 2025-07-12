from collections import deque


def main():
	n, m = [int(i) for i in input().split()]
	x = [int(i) for i in input().split()]

	if n == m:
		print(0)
		exit()
	if m == 1:
		print(max(x) - min(x))
		exit()

	x = list(set(x))
	x.sort()
	n = len(x)

	diff = []
	for i in range(n - 1):
		diff.append(x[i + 1] - x[i])
	diff.sort()
	diff = deque(diff)

	result = 0
	while n > m:
		result += diff.popleft()
		n -= 1

	print(result)


if __name__ == "__main__":
	main()

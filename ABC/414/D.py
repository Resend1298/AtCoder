from collections import deque


def main():
	_, m = [int(i) for i in input().split()]
	x = list(set([int(i) for i in input().split()]))
	n = len(x)

	if m >= n:
		print(0)
		exit()
	if m == 1:
		print(max(x) - min(x))
		exit()

	x.sort()
	diff = []
	for i in range(1, n):
		diff.append(x[i] - x[i - 1])
	diff.sort()
	diff = deque(diff)

	result = 0
	while n > m:
		result += diff.popleft()
		n -= 1
	print(result)


if __name__ == "__main__":
	main()

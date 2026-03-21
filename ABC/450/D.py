from collections import deque


def main():
	n, k = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	for i in range(n):
		a[i] %= k
	a.sort()
	a = deque(a)

	result = a[-1] - a[0]

	for _ in range(n - 1):
		a.append(a.popleft() + k)
		result = min(result, a[-1] - a[0])

	print(result)


if __name__ == "__main__":
	main()

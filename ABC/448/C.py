from sortedcontainers import SortedList


def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	balls = SortedList(a)

	for _ in range(q):
		_ = int(input())
		b = [int(i) - 1 for i in input().split()]

		for i in b:
			balls.remove(a[i])
		print(balls[0])
		for i in b:
			balls.add(a[i])


if __name__ == "__main__":
	main()

from sortedcontainers import SortedList


def main():
	n = int(input())
	a = SortedList([int(i) for i in input().split()])

	for i in range(n, -1, -1):
		if n - a.bisect_left(i) >= i:
			print(i)
			exit()


if __name__ == "__main__":
	main()

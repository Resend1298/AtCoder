from sortedcontainers import SortedList


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	sl = SortedList()
	sl.add(a[0])
	sl.add(a[1])

	for i in range(2, n):
		sl.add(a[i])
		print(sl[-3])


if __name__ == "__main__":
	main()

from sortedcontainers import SortedList


def main():
	x = int(input())
	q = int(input())

	sl = SortedList()
	sl.add(x)

	for _ in range(q):
		a, b = [int(i) for i in input().split()]
		sl.add(a)
		sl.add(b)
		print(sl[len(sl) // 2])


if __name__ == "__main__":
	main()

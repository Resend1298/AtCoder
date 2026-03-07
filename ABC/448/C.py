from sortedcontainers import SortedList


def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	bag = SortedList(a)

	for _ in range(q):
		k = int(input())
		b = [int(i) for i in input().split()]

		remove = [a[i - 1] for i in b]

		for i in remove:
			bag.remove(i)
		print(bag[0])
		for i in remove:
			bag.add(i)


if __name__ == "__main__":
	main()

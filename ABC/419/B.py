from sortedcontainers import SortedList


def main():
	q = int(input())

	bag = SortedList()

	for _ in range(q):
		query = [int(i) for i in input().split()]

		match query[0]:
			case 1:
				bag.add(query[1])
			case 2:
				print(bag.pop(0))


if __name__ == "__main__":
	main()

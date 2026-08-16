# TODO: review

from sortedcontainers import SortedList


def main():
	q, v = [int(i) for i in input().split()]

	batteries = SortedList()

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, t, w:
				batteries.add(w - t)
			case 2, t:
				if batteries:
					print(min(v, batteries.pop() + t))
				else:
					print(-1)


if __name__ == "__main__":
	main()

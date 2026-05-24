# TODO: review

from sortedcontainers import SortedList


def main():
	n, q = [int(i) for i in input().split()]

	current = [0] * n
	remove_count = 0
	sl = SortedList([0] * n)

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, x:
				x -= 1
				sl.remove(current[x])
				current[x] += 1
				sl.add(current[x])

				if sl[0] >= remove_count + 1:
					remove_count += 1
			case 2, y:
				index = sl.bisect_left(y + remove_count)
				print(n - index)


if __name__ == "__main__":
	main()

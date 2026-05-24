from sortedcontainers import SortedList


def main():
	n, q = [int(i) for i in input().split()]

	count = [0] * n
	count_sl = SortedList([0] * n)
	removed_count = 0

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, x:
				x -= 1

				count_sl.remove(count[x])
				count[x] += 1
				count_sl.add(count[x])

				if count_sl[0] - removed_count >= 1:
					removed_count += 1
			case 2, y:
				index = count_sl.bisect_left(y + removed_count)
				print(n - index)


if __name__ == "__main__":
	main()

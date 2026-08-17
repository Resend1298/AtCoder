from sortedcontainers import SortedList


def main():
	q, v = [int(i) for i in input().split()]

	batteries = SortedList()

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, t, w:
				batteries.add(w - t)
			case 2, t:
				if not batteries:
					print(-1)
					continue
				print(min(v, batteries.pop() + t))


if __name__ == "__main__":
	main()

from sortedcontainers import SortedList


def solve():
	n = int(input())
	r = [int(i) for i in input().split()]

	sortedlist_r = SortedList(enumerate(r), key=lambda x: (x[1], x[0]))
	result = 0

	while sortedlist_r:
		index, value = sortedlist_r.pop(0)
		if index + 1 < n and r[index + 1] - value > 1:
			result += r[index + 1] - (value + 1)
			sortedlist_r.remove((index + 1, r[index + 1]))
			sortedlist_r.add((index + 1, value + 1))
			r[index + 1] = value + 1
		if index - 1 >= 0 and r[index - 1] - value > 1:
			result += r[index - 1] - (value + 1)
			sortedlist_r.remove((index - 1, r[index - 1]))
			sortedlist_r.add((index - 1, value + 1))
			r[index - 1] = value + 1

	print(result)


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

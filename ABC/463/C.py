from sortedcontainers import SortedDict


def main():
	n = int(input())
	hl = [[int(i) for i in input().split()] for _ in range(n)]
	_ = int(input())
	t = [int(i) for i in input().split()]

	# only the tallest person for a given L is needed
	lh = {}
	for h, l in hl:
		lh[l] = max(lh.get(l, float("-inf")), h)
	hl = [(h, l) for l, h in lh.items()]
	hl.sort(key=lambda x: x[1])

	tallest_at_time = {}
	current_tallest = float("-inf")
	for h, l in hl[::-1]:
		tallest_at_time[l + 1] = current_tallest
		current_tallest = max(current_tallest, h)
	tallest_at_time[0] = current_tallest
	tallest_at_time = SortedDict(tallest_at_time)

	for i in t:
		index = tallest_at_time.bisect_right(i + 1) - 1
		print(tallest_at_time.peekitem(index)[1])


if __name__ == "__main__":
	main()

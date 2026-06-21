# TODO: review

from sortedcontainers import SortedKeyList


def main():
	n = int(input())
	hl = [[int(i) for i in input().split()] for _ in range(n)]
	q = int(input())
	t = [int(i) for i in input().split()]

	hl_sl = SortedKeyList(hl, key=lambda x: (x[0], x[1]))
	changed = {}
	max_h = hl_sl[-1][0]
	changed[0] = max_h
	for h, l in hl:
		hl_sl.remove([h, l])
		if hl_sl:
			changed[l] = hl_sl[-1][0]
	changed = SortedKeyList(changed.items(), key=lambda x: x[0])

	for i in t:
		index = changed.bisect_key_right(i) - 1
		print(changed[index][1])


if __name__ == "__main__":
	main()

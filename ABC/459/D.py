from collections import Counter

from sortedcontainers import SortedKeyList


def solve():
	s = input()

	s_counter = Counter(s)
	remaining = SortedKeyList(s_counter.items(), key=lambda x: x[1])

	result = []
	while remaining:
		if len(remaining) == 1 and result and result[-1] == remaining[0][0]:
			print("No")
			return

		for i in range(len(remaining) - 1, -1, -1):
			if not result or result[-1] != remaining[i][0]:
				result.append(remaining[i][0])
				char, count = remaining.pop(i)
				if count - 1 > 0:
					remaining.add((char, count - 1))
				break

	print("Yes")
	print(''.join(result))


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

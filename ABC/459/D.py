# CPython TLE, PyPy AC

from collections import Counter

from sortedcontainers import SortedKeyList


def solve():
	s = input()

	available = Counter(s)
	available = SortedKeyList(available.items(), key=lambda x: x[1])

	result = []
	while available:
		if len(available) == 1 and result and available[0][0] == result[-1]:
			print("No")
			return

		if not result or available[-1][0] != result[-1]:
			char, count = available.pop()
		else:
			char, count = available.pop(-2)

		result.append(char)
		count -= 1
		if count > 0:
			available.add((char, count))

	print("Yes")
	print(''.join(result))


def main():
	t = int(input())
	for _ in range(t):
		solve()


if __name__ == "__main__":
	main()

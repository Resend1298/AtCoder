# TODO: review

from sortedcontainers import SortedList


def main():
	n = int(input())
	s = input()

	diff = [0]
	for i in s:
		if i == 'A':
			diff.append(diff[-1] + 1)
		elif i == 'B':
			diff.append(diff[-1] - 1)
		else:
			diff.append(diff[-1])

	remain = SortedList(diff)

	result = 0

	for i in diff[:-1]:
		remain.remove(i)
		index = remain.bisect_left(i + 1)
		if index != len(remain):
			result += len(remain) - index

	print(result)


if __name__ == "__main__":
	main()

from sortedcontainers import SortedList


def main():
	_ = int(input())
	s = input()

	diff = [0]
	for i in s:
		if i == 'A':
			diff.append(diff[-1] + 1)
		elif i == 'B':
			diff.append(diff[-1] - 1)
		else:
			diff.append(diff[-1])

	remaining = SortedList(diff)
	result = 0

	for i in diff[:-1]:
		remaining.remove(i)
		index = remaining.bisect_left(i + 1)
		if index != len(remaining):
			result += len(remaining) - index

	print(result)


if __name__ == "__main__":
	main()

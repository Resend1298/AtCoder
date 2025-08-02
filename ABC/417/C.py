from sortedcontainers import SortedList


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	tmp_1, tmp_2 = SortedList(), SortedList()
	for i in range(n):
		tmp_1.add(i + 1 - a[i])
		tmp_2.add(i + 1 + a[i])

	result = 0
	for i in tmp_1:
		if i in tmp_2:
			result += tmp_2.count(i)

	print(result)


if __name__ == "__main__":
	main()

from sortedcontainers import SortedList


def lis_len(list_):
	lis = SortedList()
	for i in list_:
		if not lis or lis[-1] < i:
			lis.add(i)
		else:
			index = lis.bisect_left(i)
			del lis[index]
			lis.add(i)
	return len(lis)


def main():
	n = int(input())
	ab = [[int(i) for i in input().split()] for _ in range(n)]

	ab.sort(key=lambda x: (x[0], -x[1]))
	b = [i[1] for i in ab]
	print(lis_len(b))


if __name__ == "__main__":
	main()

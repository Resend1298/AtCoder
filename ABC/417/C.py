from sortedcontainers import SortedList


def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	# j-i=Ai+Aj -> i+Ai=j-Aj
	x = [i + a[i] for i in range(n)]
	y = SortedList([i - a[i] for i in range(n)])
	result = 0

	for i in x:
		result += y.count(i)

	print(result)


if __name__ == "__main__":
	main()

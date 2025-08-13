from sortedcontainers import SortedList


def main():
	n, q = [int(i) for i in input().split()]
	a = SortedList([int(i) for i in input().split()])

	sum_a = []
	tmp = 0
	for i in a:
		tmp += i
		sum_a.append(tmp)

	for _ in range(q):
		b = int(input())

		if b > a[-1]:
			print(-1)
			continue

		smaller_than_b = a.bisect_left(b) - 1
		result = sum_a[smaller_than_b] if smaller_than_b != -1 else 0
		result += (b - 1) * (n - smaller_than_b - 1)
		result += 1

		print(result)


if __name__ == "__main__":
	main()

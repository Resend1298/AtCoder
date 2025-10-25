from collections import Counter


def main():
	n, m, c = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	a = Counter(a).most_common()
	a.sort(key=lambda x: x[0])

	total = a[0][1]
	current = 0
	sum_a = []
	for start in range(len(a)):
		if start != 0:
			total -= a[start - 1][1]
		while current + 1 < len(a) and total < c:
			current += 1
			total += a[current][1]
		if current == len(a) - 1:
			current = -1
		while total < c:
			current += 1
			total += a[current][1]

		sum_a.append(total)

	result = 0
	for i in range(1, len(a)):
		result += (a[i][0] - a[i - 1][0]) * sum_a[i]
	result += (m - a[-1][0] + a[0][0]) * sum_a[0]
	print(result)


if __name__ == "__main__":
	main()

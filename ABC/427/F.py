from collections import Counter


def main():
	n, m = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	result = 1

	for start in range(n):
		included = Counter({a[start]: 1})
		not_included = Counter()

		if a[start] == 0:
			result += 1

		for i in range(start + 1, n):
			new_included = Counter()
			for j, count in not_included.items():
				tmp = (j + a[i]) % m
				if tmp == 0:
					result += count
				new_included[tmp] = count
			new_not_included = not_included + included
			included = new_included
			not_included = new_not_included

	print(result)


if __name__ == "__main__":
	main()

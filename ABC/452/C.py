from collections import defaultdict


def main():
	n = int(input())
	a, b = zip(*[(i, j - 1) for i, j in [[int(i) for i in input().split()] for _ in range(n)]])
	m = int(input())
	s = [input() for _ in range(m)]

	available = defaultdict(lambda: defaultdict(set))
	for i in s:
		for j in range(len(i)):
			available[len(i)][j].add(i[j])

	for i in s:
		if len(i) != n:
			print("No")
			continue

		for j in range(n):
			if i[j] not in available[a[j]][b[j]]:
				print("No")
				break
		else:
			print("Yes")


if __name__ == "__main__":
	main()

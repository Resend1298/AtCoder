from collections import defaultdict


def main():
	n = int(input())
	a = []
	b = []
	for _ in range(n):
		tmp = [int(i) for i in input().split()]
		a.append(tmp[0])
		b.append(tmp[1])
	m = int(input())
	s = [input() for _ in range(m)]

	check = defaultdict(lambda: defaultdict(set))
	for i in s:
		for j in range(len(i)):
			check[len(i)][j].add(i[j])

	for i in range(m):
		if len(s[i]) != n:
			print("No")
			continue

		for j in range(n):
			if s[i][j] not in check[a[j]][b[j] - 1]:
				print("No")
				break
		else:
			print("Yes")


if __name__ == "__main__":
	main()

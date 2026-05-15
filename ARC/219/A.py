from sortedcontainers import SortedKeyList


def main():
	n, m = [int(i) for i in input().split()]
	s = [[int(i) for i in list(input())] for _ in range(n)]

	q = SortedKeyList(key=lambda x: len(x[2]))
	for index in range(m):
		set_0 = {i for i in range(n) if s[i][index] == 0}
		set_1 = {i for i in range(n) if s[i][index] == 1}
		q.add((index, 0, set_0))
		q.add((index, 1, set_1))

	satisfied = set()
	used = [False] * m
	result = [0] * m
	while q:
		index, value, changes = q.pop()

		if used[index]:
			continue

		satisfied |= changes
		used[index] = True
		result[index] = value

		q = SortedKeyList([(i, j, k - changes) for i, j, k in q], key=lambda x: len(x[2]))

	if satisfied == {i for i in range(n)}:
		print("Yes")
		print(''.join(str(i) for i in result))
	else:
		print("No")


if __name__ == "__main__":
	main()

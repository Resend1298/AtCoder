# TODO: review

from sortedcontainers import SortedKeyList


def main():
	n, m = [int(i) for i in input().split()]
	s = [[int(i) for i in list(input())] for _ in range(n)]

	q = SortedKeyList(key=lambda x: len(x[2]))
	for i in range(m):
		for j in [0, 1]:
			tmp_set = set()
			for k in range(n):
				if s[k][i] == j:
					tmp_set.add(k)
			q.add((i, j, tmp_set))

	used = [False] * m
	result = [0] * m
	remaining = {i for i in range(n)}
	while q:
		current_index, current_char, current_set = q.pop()
		if used[current_index]:
			continue
		used[current_index] = True
		result[current_index] = current_char
		remaining -= current_set
		new_q = SortedKeyList(key=lambda x: len(x[2]))
		for i in q:
			new_q.add((i[0], i[1], i[2] - current_set))
		q = new_q

	if remaining:
		print("No")
	else:
		print("Yes")
		print(''.join(str(i) for i in result))


if __name__ == "__main__":
	main()

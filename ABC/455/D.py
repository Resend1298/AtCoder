def main():
	n, q = [int(i) for i in input().split()]

	father: list[int | None] = [None] * n
	top = set(range(n))

	for _ in range(q):
		c, p = [int(i) - 1 for i in input().split()]

		if father[c] is not None:
			# noinspection PyTypeChecker
			top.add(father[c])
		top.remove(p)
		father[c] = p

	result = [0] * n
	for i in top:
		current = 1
		while father[i] is not None:
			current += 1
			# noinspection PyTypeChecker
			i: int = father[i]
		result[i] = current

	print(*result)


if __name__ == "__main__":
	main()

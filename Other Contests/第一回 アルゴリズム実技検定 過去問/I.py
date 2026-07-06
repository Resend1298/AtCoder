def main():
	n, m = [int(i) for i in input().split()]
	s: list[int] = []
	c: list[int] = []
	for _ in range(m):
		tmp_s, tmp_c = input().split()
		s.append(sum(2 ** i for i in range(n) if tmp_s[i] == 'Y'))
		c.append(int(tmp_c))

	cost = [float("inf")] * (2 ** n)
	cost[0] = 0

	for i in range(m):
		for j in range(2 ** n):
			cost[j | s[i]] = min(cost[j | s[i]], cost[j] + c[i])

	print(cost[-1] if cost[-1] != float("inf") else -1)


if __name__ == "__main__":
	main()

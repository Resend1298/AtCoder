def main():
	n = int(input())
	pab = [[int(i) for i in input().split()] for _ in range(n)]

	pre = [-1] * n
	for i in range(n - 1, -1, -1):
		x = 0
		for j in range(i, n):
			if x == 0 and pre[j] != -1:
				x = pre[j]
				break

			p, a, b = pab[j]
			if p >= x:
				x += a
			else:
				x -= b
				x = max(x, 0)
		pre[i] = x

	pre_2 = [{} for _ in range(n)]

	q = int(input())
	for _ in range(q):
		x = int(input())
		tmp = []

		for i in range(n):
			if x == 0:
				x = pre[i]
				break

			if x in pre_2[i]:
				x = pre_2[i][x]
				break

			tmp.append(x)

			p, a, b = pab[i]
			if p >= x:
				x += a
			else:
				x -= b
				x = max(x, 0)

		print(x)

		for i in range(len(tmp)):
			pre_2[i][tmp[i]] = x


if __name__ == "__main__":
	main()

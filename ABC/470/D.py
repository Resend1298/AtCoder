def main():
	n, q = [int(i) for i in input().split()]
	p = [int(i) for i in input().split()]

	point_to = [-1] * (n + 1)
	point_rev = [-1] * (n + 1)
	rev = False

	for i in range(n):
		point_to[i + 1] = p[i]
		point_rev[p[i]] = i + 1

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, x, y:
				if not rev:
					tmp1, tmp2 = point_to[x], point_to[y]
					point_to[x], point_to[y] = point_to[y], point_to[x]
					point_rev[tmp1], point_rev[tmp2] = point_rev[tmp2], point_rev[tmp1]
				else:
					tmp1, tmp2 = point_rev[x], point_rev[y]
					point_rev[x], point_rev[y] = point_rev[y], point_rev[x]
					point_to[tmp1], point_to[tmp2] = point_to[tmp2], point_to[tmp1]
			case 2,:
				rev = not rev

	result = [-1] * (n + 1)
	if not rev:
		for i in range(1, n + 1):
			result[i] = point_to[i]
	else:
		for i in range(1, n + 1):
			result[i] = point_rev[i]
	print(*result[1:])


if __name__ == "__main__":
	main()

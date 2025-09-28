def main():
	n, q = [int(i) for i in input().split()]
	a = [int(i) for i in input().split()]

	shift = 0
	sum_a = [0]
	for i in a:
		sum_a.append(sum_a[-1] + i)

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case [1, c]:
				shift += c
				shift %= n
			case [2, l, r]:
				l = (l - 1 + shift) % n
				r = (r - 1 + shift) % n
				if l <= r:
					print(sum_a[r + 1] - sum_a[l])
				else:
					print(sum_a[-1] - sum_a[l] + sum_a[r + 1])


if __name__ == "__main__":
	main()

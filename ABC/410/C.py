def main():
	n, q = [int(i) for i in input().split()]
	a = [i for i in range(1, n + 1)]
	shift = 0

	for _ in range(q):
		query = [int(i) for i in input().split()]

		match query[0]:
			case 1:
				a[(query[1] - 1 + shift) % n] = query[2]
			case 2:
				print(a[(query[1] - 1 + shift) % n])
			case 3:
				shift += query[1]
				shift %= n


if __name__ == "__main__":
	main()

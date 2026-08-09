def main():
	n, q = [int(i) for i in input().split()]

	a = [0] * n
	current = 0
	positive_index = set()

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, x:
				current ^= a[x - 1]
				a[x - 1] += 1
				positive_index.add(x - 1)
				current ^= a[x - 1]
			case 2,:
				for i in positive_index.copy():
					current ^= a[i]
					a[i] -= 1
					if a[i] == 0:
						positive_index.remove(i)
					current ^= a[i]

		print(current)


if __name__ == "__main__":
	main()

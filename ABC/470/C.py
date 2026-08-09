# TODO: review

def main():
	n, q = [int(i) for i in input().split()]

	current = 0
	a = [0] * n
	not_zero = set()

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, x:
				current ^= a[x - 1]
				a[x - 1] += 1
				current ^= a[x - 1]
				not_zero.add(x - 1)
			case 2,:
				changes = set()
				for i in not_zero:
					current ^= a[i]
					a[i] -= 1
					current ^= a[i]
					if a[i] == 0:
						changes.add(i)
				not_zero -= changes

		print(current)


if __name__ == "__main__":
	main()

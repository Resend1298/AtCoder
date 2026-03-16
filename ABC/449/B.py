def main():
	h, w, q = [int(i) for i in input().split()]

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, r:
				print(r * w)
				h -= r
			case 2, c:
				print(c * h)
				w -= c


if __name__ == "__main__":
	main()

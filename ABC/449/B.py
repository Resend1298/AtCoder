# TODO: review

def main():
	h, w, q = [int(i) for i in input().split()]

	for _ in range(q):
		match [int(i) for i in input().split()]:
			case 1, r:
				print(w * r)
				h -= r
			case 2, c:
				print(h * c)
				w -= c


if __name__ == "__main__":
	main()

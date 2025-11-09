def main():
	x = int(input())
	n = int(input())
	w = [int(i) for i in input().split()]
	q = int(input())

	attached = [False] * n

	for _ in range(q):
		p = int(input()) - 1

		if attached[p]:
			x -= w[p]
			attached[p] = False
		else:
			x += w[p]
			attached[p] = True

		print(x)


if __name__ == "__main__":
	main()

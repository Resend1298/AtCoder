# TODO: review

def main():
	x = int(input())
	n = int(input())
	w = [int(i) for i in input().split()]
	q = int(input())

	attached = [False] * n

	for _ in range(q):
		p = int(input()) - 1
		if not attached[p]:
			attached[p] = True
			x += w[p]
		else:
			attached[p] = False
			x -= w[p]
		print(x)


if __name__ == "__main__":
	main()

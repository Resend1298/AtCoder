from math import ceil


def main():
	n, h = [int(i) for i in input().split()]
	a, b = [], []
	for _ in range(n):
		tmp = [int(i) for i in input().split()]
		a.append(tmp[0])
		b.append(tmp[1])

	max_a = max(a)
	b = [i for i in b if i > max_a]
	b.sort(reverse=True)

	for i in range(len(b)):
		h -= b[i]
		if h <= 0:
			print(i + 1)
			break
	else:
		print(len(b) + ceil(h / max_a))


if __name__ == "__main__":
	main()

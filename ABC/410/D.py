# TODO: WA

def main():
	n, m = [int(i) for i in input().split()]
	edge = []
	for _ in range(m):
		a, b, w = [int(i) for i in input().split()]
		edge.append((a - 1, b - 1, w))

	d = [-1] * n
	d[0] = 0

	while True:
		update = False
		for x, y, z in edge:
			if d[x] != -1 and (d[y] > d[x] ^ z or d[y] == -1):
				d[y] = d[x] ^ z
				update = True
		if not update:
			break

	print(d[n - 1])


if __name__ == "__main__":
	main()

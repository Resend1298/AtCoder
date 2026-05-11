def main():
	n, k = [int(i) for i in input().split()]
	l = []
	a = []
	for _ in range(n):
		la = [int(i) for i in input().split()]
		l.append(la[0])
		a.append(la[1:])
	c = [int(i) for i in input().split()]

	for i in range(n):
		if k > l[i] * c[i]:
			k -= l[i] * c[i]
			continue

		k = (k - 1) % l[i]
		print(a[i][k])
		break


if __name__ == "__main__":
	main()

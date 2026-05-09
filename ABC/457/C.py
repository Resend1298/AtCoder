def main():
	n, k = [int(i) for i in input().split()]
	a = [[int(i) for i in input().split()] for _ in range(n)]
	c = [int(i) for i in input().split()]

	for i in range(n):
		if k > a[i][0] * c[i]:
			k -= a[i][0] * c[i]
		else:
			k = (k - 1) % a[i][0]
			print(a[i][k + 1])
			exit()


if __name__ == "__main__":
	main()

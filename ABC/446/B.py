def main():
	n, m = [int(i) for i in input().split()]
	l = []
	x = []
	for _ in range(n):
		l.append(int(input()))
		x.append([int(i) - 1 for i in input().split()])

	available = [True] * m

	for i in x:
		for j in i:
			if available[j]:
				available[j] = False
				print(j + 1)
				break
		else:
			print(0)


if __name__ == "__main__":
	main()

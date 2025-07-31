def main():
	n = int(input())
	a, b = [], []
	for _ in range(n):
		tmp = [int(i) for i in input().split()]
		a.append(tmp[0])
		b.append(tmp[1])

	speech = [2 * a[i] + b[i] for i in range(n)]
	speech.sort(reverse=True)
	diff = -sum(a)

	for i in range(n):
		diff += speech[i]
		if diff > 0:
			print(i + 1)
			break


if __name__ == "__main__":
	main()

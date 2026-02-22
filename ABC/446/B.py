# TODO: review

def main():
	n, m = [int(i) for i in input().split()]
	l = []
	x = []
	for _ in range(n):
		l.append(int(input()))
		x.append([int(i) - 1 for i in input().split()])

	result = []
	chosen = [False] * m

	for i in range(n):
		for j in x[i]:
			if not chosen[j]:
				chosen[j] = True
				result.append(j + 1)
				break
		else:
			result.append(0)

	for i in result:
		print(i)


if __name__ == "__main__":
	main()

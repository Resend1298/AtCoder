def main():
	h, w, n = [int(i) for i in input().split()]
	a = [[int(i) for i in input().split()] for _ in range(h)]
	b = set(int(input()) for _ in range(n))

	result = 0

	for i in a:
		tmp = 0
		for j in i:
			if j in b:
				tmp += 1
		result = max(result, tmp)

	print(result)


if __name__ == "__main__":
	main()

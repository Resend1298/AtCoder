def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	result = 0

	for l in range(n):
		for r in range(l, n):
			sum_lr = sum(a[l:r + 1])
			for i in a[l:r + 1]:
				if sum_lr % i == 0:
					break
			else:
				result += 1

	print(result)


if __name__ == "__main__":
	main()

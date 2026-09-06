def main():
	n = int(input())
	a = [int(i) for i in input().split()]
	b = [int(i) for i in input().split()]

	diff_plus = 0
	diff_minus = 0
	for i in range(n):
		if a[i] > b[i]:
			diff_plus += a[i] - b[i]
		elif a[i] < b[i]:
			diff_minus += b[i] - a[i]

	if diff_plus * 10 ** 18 > diff_minus:
		print("Yes")
	else:
		print("No")
		exit()

	result = []
	for i in range(n):
		if a[i] > b[i]:
			result.append(10 ** 18)
		elif a[i] < b[i]:
			result.append(1)
		else:
			result.append(1)

	print(*result)


if __name__ == "__main__":
	main()

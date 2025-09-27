def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	a_count = [0] * n
	for i in a:
		if i != -1:
			a_count[i - 1] += 1

	if max(a_count) > 1:
		print("No")
		exit()

	usable_number = []
	for i in range(n):
		if a_count[i] == 0:
			usable_number.append(i + 1)

	result = []
	for i in range(n):
		if a[i] != -1:
			result.append(a[i])
		else:
			result.append(usable_number.pop())

	print("Yes")
	print(*result)


if __name__ == "__main__":
	main()

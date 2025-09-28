def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	usable_number = set(range(1, n + 1))

	for i in a:
		if i == -1:
			continue
		if i in usable_number:
			usable_number.remove(i)
		else:
			print("No")
			exit()

	result = []
	for i in a:
		if i == -1:
			result.append(usable_number.pop())
		else:
			result.append(i)

	print("Yes")
	print(*result)


if __name__ == "__main__":
	main()

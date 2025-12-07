def main():
	n = int(input())
	a = [int(i) for i in input().split()]

	current_range = 1

	for i in range(1, n + 1):
		if i > current_range:
			print(i - 1)
			break

		current_range = max(current_range, i + a[i - 1] - 1)
	else:
		print(n)


if __name__ == "__main__":
	main()

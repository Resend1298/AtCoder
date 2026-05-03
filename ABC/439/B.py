def operation(x):
	x_digits = [int(i) for i in str(x)]
	return sum(i ** 2 for i in x_digits)


def main():
	n = int(input())

	visited = set()

	while n not in visited and n != 1:
		visited.add(n)
		n = operation(n)

	print("Yes" if n == 1 else "No")


if __name__ == "__main__":
	main()

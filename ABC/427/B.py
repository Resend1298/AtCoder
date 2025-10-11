def f(x):
	return sum([int(i) for i in list(str(x))])


def main():
	n = int(input())

	current = f(1)
	a = [1]

	for _ in range(1, n + 1):
		a.append(current)
		current += f(a[-1])

	print(a[-1])


if __name__ == "__main__":
	main()

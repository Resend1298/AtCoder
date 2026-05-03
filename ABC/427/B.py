def f(x):
	return sum(int(i) for i in list(str(x)))


def main():
	n = int(input())

	a = 1
	sum_f = f(a)

	for _ in range(1, n + 1):
		a = sum_f
		sum_f += f(a)

	print(a)


if __name__ == "__main__":
	main()

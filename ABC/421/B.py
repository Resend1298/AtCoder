def f(x):
	return int(str(x)[::-1])


def main():
	a = [int(i) for i in input().split()]

	for i in range(2, 10):
		a.append(f(a[i - 2] + a[i - 1]))

	print(a[9])


if __name__ == "__main__":
	main()

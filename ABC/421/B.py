# TODO: review

def main():
	x, y = [int(i) for i in input().split()]

	a = [x, y]

	for i in range(2, 10):
		tmp = a[i - 1] + a[i - 2]
		a.append(int(str(tmp)[::-1]))

	print(a[9])


if __name__ == "__main__":
	main()

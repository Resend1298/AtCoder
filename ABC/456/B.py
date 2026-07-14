def main():
	a = [[int(i) for i in input().split()] for _ in range(3)]

	count = 0
	for i in a[0]:
		for j in a[1]:
			for k in a[2]:
				if {i, j, k} == {4, 5, 6}:
					count += 1

	print(count / 6 ** 3)


if __name__ == "__main__":
	main()

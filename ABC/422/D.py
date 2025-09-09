def main():
	n, k = [int(i) for i in input().split()]

	if k % (2 ** n) == 0:
		print(0)
		print(*[k // (2 ** n)] * (2 ** n))
	else:
		print(1)

		x = [k]
		for _ in range(n):
			new_x = []
			for i in x:
				new_x.append(i // 2)
				new_x.append(i - i // 2)
			x = new_x

		print(*x)


if __name__ == "__main__":
	main()

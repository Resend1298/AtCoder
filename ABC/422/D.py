# TODO: review

def main():
	n, k = [int(i) for i in input().split()]

	match k % (2 ** n):
		case 0:
			print(0)
			print(*[k // (2 ** n)] * (2 ** n))
		case _:
			print(1)

			x = [k // 2, k - k // 2]
			for _ in range(n - 1):
				new_x = []
				for i in x:
					new_x.append(i // 2)
					new_x.append(i - i // 2)
				x = new_x
			print(*x)


if __name__ == "__main__":
	main()

def main():
	m, d = [int(i) for i in input().split()]

	match m, d:
		case (1, 7) | (3, 3) | (5, 5) | (7, 7) | (9, 9):
			print("Yes")
		case _:
			print("No")


if __name__ == "__main__":
	main()

def main():
	a, b = [int(i) for i in input().split()]

	if a + b == 9 or a - b == 9 or a * b == 9 or a == b * 9:
		print("Nine")
	else:
		# noinspection SpellCheckingInspection
		print("Nein")


if __name__ == "__main__":
	main()

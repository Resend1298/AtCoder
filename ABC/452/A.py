def main():
	m, d = [int(i) for i in input().split()]
	festivals = {(1, 7), (3, 3), (5, 5), (7, 7), (9, 9)}

	if (m, d) in festivals:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

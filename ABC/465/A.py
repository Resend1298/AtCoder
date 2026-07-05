# TODO: review

def main():
	a, b = [int(i) for i in input().split()]

	if a * 3 > b * 2:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

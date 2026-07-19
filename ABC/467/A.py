# TODO: review

def main():
	h, w = [int(i) for i in input().split()]

	if w * 100 * 100 >= 25 * h * h:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

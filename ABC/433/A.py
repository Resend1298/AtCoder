# TODO: review

def main():
	x, y, z = [int(i) for i in input().split()]

	if (x - y * z) % (z - 1) == 0 and x - y * z >= 0:
		print("Yes")
	else:
		print("No")


if __name__ == "__main__":
	main()

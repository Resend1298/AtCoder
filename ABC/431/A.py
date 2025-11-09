def main():
	h, b = [int(i) for i in input().split()]

	if b >= h:
		print(0)
	else:
		print(h - b)


if __name__ == "__main__":
	main()
